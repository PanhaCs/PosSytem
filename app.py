from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('user/home.html')



product_list = [
        {
            'id' : '1',
            'title' : 'Jordan',
            'price' : '200',
            'description' : "Some quick example text to build on the card title and make up the bulk of the card's content.",
            'image': 'shoe2.jpg'
        },
        {
            'id' : '2',
            'title' : 'Nike',
            'price' : '150',
            'description' : "Some quick example text to build on the card title and make up the bulk of the card's content.",
            'image': 'shoe3.jpg'
        }
    ]


@app.route('/product')
def product():
    return render_template('user/product.html', product_list = product_list)



@app.route('/product_detail')
def product_detail():
    product_id = request.args.get('id')
    current_product = []
    for item in product_list:
        if item['id'] == product_id:
            current_product = item
            
    return render_template('user/product_detail.html',current_product=current_product)



@app.route('/checkout')
def checkout():
    product_id = request.args.get('id')
    current_product = []
    for item in product_list:
        if item['id'] == product_id:
            current_product = item
            
    return render_template('user/checkout.html',current_product=current_product)



if __name__ == '__main__':
    app.run()
