import unittest
from Animal import *


class TestMyAnimals(unittest.TestCase):

   def test_animal_tail(self):
       self.assertEqual(lion.tail, 1)

   def test_animal_woof(self):
       self.assertTrue(lion.wool)

   def test_animal_paw(self):
       self.assertEqual(lion.paw, 4)

   def test_animal_incorrect_tail(self):
       self.assertEqual(lion.tail, 2)

   def test_animal_incorrect_woof(self):
       self.assertFalse(lion.wool)

   def test_animal_incorrect_paw(self):
       self.assertEqual(lion.paw, 3)

   def test_dog_tail(self):
       self.assertEqual(dog.tail, 1)

   def test_dog_paw(self):
       self.assertEqual(dog.paw, 4)

   def test_dog_wool(self):
       self.assertTrue(dog.wool)

   def test_wrong_dog_tail(self):
       self.assertEqual(dog.tail, 2)

   def test_wrong_dog_paw(self):
       self.assertEqual(dog.paw, 3)

   def test_wrong_dog_woof(self):
       self.assertFalse(dog.woof)

   def test_dog_woof(self):
       self.assertTrue(dog.say_woof())

   def test_dog_no_woof(self):
       self.assertFalse(dog.say_woof())

   def test_cat_paw(self):
       self.assertEqual(cat1.paw, 4)

   def test_cat_wool(self):
       self.assertTrue(cat1.wool)

   def test_cat_tail(self):
       self.assertEqual(cat1.tail, 1)

   def test_cat_incorrect_paw(self):
       self.assertEqual(cat1.paw, 2)

   def test_cat_incorrect_wool(self):
       self.assertFalse(cat1.wool)

   def test_cat_incorrect_tail(self):
       self.assertEqual(cat1.tail, 2)

   def test_cat_meow(self):
       self.assertTrue(cat1.say_meow())

   def test_cat_no_meow(self):
       self.assertFalse(cat1.say_meow())

   def test_SphynxCat_paw(self):
       self.assertEqual(cat2.paw, 4)

   def test_SphynxCat_wool(self):
       self.assertTrue(cat2.wool)

   def test_SphynxCat_tail(self):
       self.assertEqual(cat2.tail, 1)

   def test_SphynxCat_incorrect_paw(self):
       self.assertEqual(cat2.paw, 2)

   def test_SphynxCat_incorrect_wool(self):
       self.assertFalse(cat2.wool)

   def test_SphynxCat_incorrect_tail(self):
       self.assertEqual(cat2.tail, 2)

   def test_SphynxCat_mur(self):
       self.assertTrue(cat2.say_murr())

   def test_SphynxCat_no_mur(self):
       self.assertFalse(cat2.say_murr())

   def test_Rooster_paw(self):
       self.assertEqual(rooster1.paw, 2)

   def test_Rooster_wool(self):
       self.assertFalse(rooster1.wool)

   def test_Rooster_tail(self):
       self.assertEqual(rooster1.tail, 1)

   def test_Rooster_incorrect_paw(self):
       self.assertEqual(rooster1.paw, 4)

   def test_Rooster_incorrect_wool(self):
       self.assertTrue(rooster1.wool)

   def test_Rooster_incorrect_tail(self):
       self.assertEqual(rooster1.tail, 3)

   def test_Rooster_coco(self):
       self.assertTrue(rooster1.say_Cocorico())

   def test_Rooster_no_coco(self):
       self.assertFalse(rooster1.say_Cocorico())

