from unittest import TestCase
from app import app


class ColorApp(TestCase):
    """test routes in our app."""

    def test_home(self):
        with app.test_client() as client:
            response = client.get("/")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<h1>Colors</h1>", html)

    def test_new_uncool_color(self):
        with app.test_client() as client:
            response = client.post("/colors", json={"color": "red"})

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"color": "red", "isCool": False})
    
    def test_new_cool_color(self):
        with app.test_client() as client:
            response = client.post("/colors", json={"color": "peachpuff"})

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"color": "peachpuff", "isCool": True})

    def test_all_cool_colors(self):
        with app.test_client() as client:
            response = client.get("/cool_colors")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json,
                {"cool_colors": ["cornsilk", "firebrick", "peachpuff"]})
