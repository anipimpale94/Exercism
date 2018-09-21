# def calculateLargestProduct(subSeries, size):
#     if len(subSeries) < size or not subSeries.isdigit():
#         return 0
#     else:
#         product = 1
#         for index in range(0,size):
#             product = product * int(subSeries[index])
        
#         recursiveResult = calculateLargestProduct(subSeries[1:], size)
#         return product if product > recursiveResult else recursiveResult

def largest_product(series, size):
    
    if size > -1:
        if size == 0:
            return 1
        if len(series) < size or not series.isdigit():
            raise ValueError('Invalid Input') 
        else:   
            # return calculateLargestProduct(series, size)

            count = 0
            product = 1
            maxProduct = 0
            temp = [1]*size
            for index in range(0, len(series)):
                if int(series[index]) == 0:
                    count = 0
                    product = 1
                else:
                    product = product * int(series[index])
                    count = count + 1                  
                    if count > size:
                        product = product / temp[1 % size] 
                    temp[1 % size] = int(series[index])      
                    if count >= size and product > maxProduct:
                        maxProduct = product             
            return int(maxProduct)
    else:
        raise ValueError('Invalid Input') 
        
largest_product("0123456789",2)