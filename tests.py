import unittest
import movie_in_theaters_imdb

class Movie_In_Theaters_Imdb_Tests(unittest.TestCase):
	
	def test_find_film_list_Has_Code_200(self):
		site = "http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1"
		result = movie_in_theaters_imdb.find_film_list(site)
		self.assertNotEqual(result, False)

if __name__ == '__main__':
    unittest.main()