# Masters India
Assignment for Masters India

## Steps to run the application:

1. Create virtual environment.
    > source venv/bin/activate

2. Install required python packages
    > pip install -r requirements.txt

3. Run the application
    > python manage.py runserver


## APIs

1. API to get all categories ( /api/category )

![output image](https://github.com/kashyapkathrani/masters-india/blob/master/ProductApp/static/category.png)

2. API to get subcategories for a category ( /api/:category_id/subcategory )

![output image](https://github.com/kashyapkathrani/masters-india/blob/master/ProductApp/static/subcategory.png)

3. API to get all products for a category ( /api/product/?category=category_id )

![output image](https://github.com/kashyapkathrani/masters-india/blob/master/ProductApp/static/product_by_category.png)

4. API to get all products for a subcategory ( /api/product/?subcategory=subcategory_id )

![output image](https://github.com/kashyapkathrani/masters-india/blob/master/ProductApp/static/product_by_subcategory.png)

5. API to post new product under existing subcategory and category ( /api/product/add )

![output image](https://github.com/kashyapkathrani/masters-india/blob/master/ProductApp/static/add_product.png)

### Super User Details
username: kashyap

password: Masters@1234
