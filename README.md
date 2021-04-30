
### filtering-products

- filtering-products is a django project built using Django, django-filter and bootstrap
- It allow users to filter products based on Product model attributes (title, product_type, height, width and price)
- To add some initial products to the database, i created script.py, based on this [product samples](https://github.com/wedeploy-examples/supermarket-web-example/blob/master/products.json), and i just have to open the shell and run the script:
    - python manage.py shell
    - from products import script
    - script.create_products()


This is a screenshot from the project:
![Image of products](https://github.com/pedrasfloki/filtering-products/blob/main/filtering-products.png)

