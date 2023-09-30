def linearSearchProduct(productList,targetproduct):
    indices =[]
  
    for index,product in enumerate(productList):
      if product == target:
        indices.append(index)
 
    return indices


products=["shoes","slipper","sandle","slipper","slipper"]
target="slipper"
result = linearSearchProduct(products,target)
print(result)