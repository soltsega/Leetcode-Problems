class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        listMap = {restaurant:i for i, restaurant in enumerate(list1)}
        output = []
        minIdx  = float('inf')

        for j, restaurant  in enumerate(list2):
            if restaurant in listMap:
                idxSum = listMap[restaurant]+j

                if idxSum<minIdx:
                    output = [restaurant]
                    minIdx = idxSum
                elif idxSum==minIdx:
                    output.append(restaurant)

        return output


        

        