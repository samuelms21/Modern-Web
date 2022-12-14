from package import app, db
from package.models import User, Invoice, InvoiceDetail, Category, Product
import socket

@app.shell_context_processor
def make_shell_context(): return {
    'db': db, 
    'User': User,
    'Invoice': Invoice,
    'InvoiceDetail': InvoiceDetail,
    'Category': Category,
    'Product': Product
    }

if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    app.run(host=ip_address, port=5000, debug=True, threaded=False)