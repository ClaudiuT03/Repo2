"""
Teste pentru endpoint-urile de products
din https://dummyjson.com/docs/products.

Aceste teste folosesc metodele ajutatoare
definite in clasa ProductsRequests,
pentru a interactiona cu API-ul.
"""
import unittest

from TA_S5_weekend_dummy_requests.dummy_json_requests.products import ProductsRequests


class TestProductsRequests(unittest.TestCase):

    def setUp(self):
        self.products_req = ProductsRequests()

    def test_get_all_products(self):
        """
        Testam endpoint-ul de baza GET (/products),
        atunci cand nu furnizam nici un parametru.

        Verificari:
        - status code este 200
        - in raspunsul json, am primit exact 30 de produse
        - cheia total are valoarea 100
        - cheia limit are valoarea 30
        - cheia skip are valoarea 0
        """
        response = self.products_req.get_products()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_msg["products"]), 30)
        self.assertEqual(response_msg["total"], 100)
        self.assertEqual(response_msg["limit"], 30)
        self.assertEqual(response_msg["skip"], 0)


    def test_get_products_when_limit_is_set(self):
        """
        Testam endpoint-ul de GET /products
        cand furnizam query param-ul limit

        Verificari:
        - status code este 200
        - in raspunsul json, am primit exact <limit> de produse
        - cheia limit are valoarea <limit>
        """
        limit = 10
        response = self.products_req.get_products(limit=limit)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_msg["products"]), limit)
        self.assertEqual(response_msg["limit"], limit)

    def test_get_products_when_skip_is_set(self):
        """
        Testam endpoint-ul de GET /products
        cand furnizam query param-ul skip

        Verificari:
        - status code este 200
        - in raspunsul json, verificam ca id-ul primului produs
        este <skip + 1>
        - cheia skip are valoarea <skip>
        :return:
        """
        skip = 5
        response = self.products_req.get_products(skip=skip)
        response_msg = response.json()
        product_id = response_msg["products"][0]["id"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product_id, skip + 1)
        self.assertEqual(response_msg["skip"], skip)


    def test_get_products_when_skip_is_greater_than_total_number_of_products(self):
        """
        Testam endpoint-ul de GET /products
        cand furnizam query param-ul skip
        si ii dam o valoare mai mare de numarul total de produse.

        Verificari:
        - status code este 200
        - in raspunsul json, avem cheia products, dar valoarea acesteia, este o lista goala.
        - cheia skip are valoarea <skip>
        """
        skip = "abc"
        response = self.products_req.get_products(skip=skip)
        response_msg = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_msg["message"], "Invalid skip limit")

    def test_get_products_when_skip_has_invalid_format(self):
        """
        Verificari:
        - status code este 400
        - verificam ca mesajul primit in response este cel asteptat
        """
        skip = "uugv"
        response = self.products_req.get_products(skip=skip)
        response_msg = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_msg["message"], "Invalid skip limit")

    def test_get_product_by_id_when_id_is_in_db(self):
        """
        Verificari:
        - status code este 200
        - in raspuns, ca pentru cheia id, avem aceeasi valoare, ca
        cea trimisa in request
        - verificam ca avem cheile: title, price, description, category,stock in response
        """
        product_id = 5
        response = self.products_req.get_product_by_id(product_id=product_id)
        self.assertEqual(response.status_code, 200)
        keys_list = ["title", "price", "description", "category", "stock"]
        response_msg = response.json()
        for key in keys_list:
            self.assertIn(key, response_msg)

    def test_get_product_by_id_when_id_is_not_in_db(self):
        """
        Verificari:
        - status code este 404
        - in raspuns, verificam mesajul
        """
        product_id = 110
        response = self.products_req.get_product_by_id(product_id=product_id)
        self.assertEqual(response.status_code, 404)
        response_msg = response.json()

        self.assertEqual(response_msg["message"], f"Product with id '{product_id}' not found")


    def test_search_product_when_products_found_by_criteria(self):
        """
        Verificari:
        - status code 200
        - verificam ca lista products NU este goala
        - total este mai mare decat 0
        - limit este mai mare decat 0
        """
        response = self.products_req.search_products(search_criteria="phone")
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response_msg["products"]), 0)
        self.assertTrue(response_msg["products"])
        self.assertGreater(response_msg["total"], 0)
        self.assertGreater(response_msg["limit"], 0)

    def test_search_product_when_products_not_found_by_criteria(self):
        """
            Verificari:
            - status code 200
            - verificam ca lista products este goala
            - total este egal cu 0
            - limit este egal cu 0
        """
        response = self.products_req.search_products(search_criteria="phonelhlhkkg")
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_msg["products"]), 0)
        self.assertFalse(response_msg["products"])
        self.assertEqual(response_msg["total"], 0)
        self.assertEqual(response_msg["limit"], 0)

    def test_add_product_with_single_key(self):
        response = self.products_req.add_product({
                "title": "Galaxy s5155555",
                "price": 1276,
                "stock": 200
            })
        return response

    def test_add_product_with_multiple_keys(self):

        response = self.products_req.add_product({
            "title": "Galaxy s5155555",
            "price": 1276,
            "stock": 200,
            "description": "An apple mobile which is nothing like apple",
            "discountPercentage": 12.96,
            "rating": 4.69
        })
        return response

    def test_add_product_with_invalid_key(self):
        response = self.products_req.add_product({
            "titlesss": "Galaxy s5155555",
            "rating": 4.69
        })
        return response

    def test_update_product(self, product_id=1):
        # product_id = 1
        response = self.products_req.update_product({
            "title": "Galaxy s5155555",
            "rating": 4.69
        })
        return response

    def test_delete_product_when_id_is_in_db(self):
        pass

    def test_delete_product_when_id_is_not_in_db(self):
        pass

