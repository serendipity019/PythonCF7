
def main():
   store_a_product = {"Apples", "Bananas", "Cherries", "Watermelons"}
   store_b_product = {"Figs", "Bananas", "Cherries", "Ggrapes", "Melons"}

   # Find common products (intersection) available in both stores
   common_products = store_a_product & store_b_product
   print(common_products)
   # Alternative way
   common_products2 = store_a_product.intersection(store_b_product)
   print(common_products2)

   # Find all unique products (union) across both stores (A and B)
   unique_products = store_a_product | store_b_product
   print(unique_products)
   # Using func
   unique_products2 = store_a_product.union(store_b_product)
   print(unique_products2)

   # Find products available in store B but not in store A (difference)
   exclusive_b_products = store_b_product - store_a_product
   print(exclusive_b_products)
   # Using functions
   exclusive_b_products2 = store_b_product.difference(store_a_product)
   print(exclusive_b_products2) 

   # find products that are in either Store A or Store B but not in both
   unique_to_either_store = store_a_product ^ store_b_product
   print(unique_to_either_store)
   # Using func
   unique_to_either_store2 = store_a_product.symmetric_difference(store_b_product)
   print(unique_to_either_store2) 


if __name__ == "__main__":
    main() 