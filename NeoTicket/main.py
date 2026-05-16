from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)  # 🛡️ 注入防跨域盾牌，允许你的前端网页跨网络调用这个接口

# 封装你之前的核心退票事务
def execute_refund_transaction(order_id, ticket_id):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',  # ⚠️ 换成你真正的 MySQL root 密码！
            database='my_ticket_db',
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        
        # 1. 开启事务
        cursor.execute("START TRANSACTION;")
        
        # 2. 归还库存
        cursor.execute("UPDATE tickets SET stock = stock + 1 WHERE id = %s;", (ticket_id,))
        
        # 3. 修改订单状态
        cursor.execute("UPDATE orders SET status = '已退款' WHERE id = %s;", (order_id,))
        
        # 4. 提交事务
        conn.commit()
        return True, f"成功为订单号【{order_id}】办理退款！"
    except Exception as e:
        if 'conn' in locals():
            conn.rollback()
        return False, str(e)
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

# ==========================================
# 🚀 定义网络路由 (Routing)：将网址映射到 Python 函数
# ==========================================
@app.route('/api/refund', methods=['POST'])
def refund_api():
    # 1. 接收前端网页发过来的 JSON 数据
    data = request.json
    order_id = data.get('order_id')
    ticket_id = data.get('ticket_id')
    
    # 2. 调用刚才的底层数据库事务
    success, message = execute_refund_transaction(order_id, ticket_id)
    
    # 3. 把处理结果打包成 JSON 回传给前端网页
    if success:
        return jsonify({"code": 200, "status": "success", "message": message})
    else:
        return jsonify({"code": 500, "status": "error", "message": f"底层事务回滚，原因: {message}"})

if __name__ == "__main__":
    # 启动 Web 服务器，监听本地 5000 端口
    print("🔮 NeoTicket Web 服务正在启动... 监听地址: http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)