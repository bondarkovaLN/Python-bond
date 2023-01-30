* Задать одномерный массив и найти в нем минимальный и максимальный
     * элементы;
     */
    static int[] minMax(int[] array) {
        int min = 0;
        int max = 0;

        for (int item : array) {
            if (item < min) min = item;
            if (item > max) max = item;
        }
        return new int[]{min, max};
    }

// 2*.Написать метод, который определяет, является ли год високосным,
    // и возвращает boolean (високосный - true, не високосный - false).
    // Каждый 4-й год является високосным, кроме каждого 100-го,
    // при этом каждый 400-й – високосный.
    public static boolean checkLeapYear (int year){
        if (year % 400 == 0){
            return true;
        } else if (year % 100 == 0) {
            return false;
        } else {
            return year % 4 == 0;
        }

    }
}
// 3..Дан массив nums = [3,2,2,3] и число val = 3.
Если в массиве есть числа, равные заданному, нужно перенести эти элементы в конец массива.
// Java program to move all values
// equal to K to the end of the Array
class GFG{
 
// Function to move the element to the end
static int[] moveElementToEnd(int []array,
                              int toMove)
{
    // Mark left pointer
    int i = 0;
 
    // Mark the right pointer
    int j = array.length - 1;
 
    // Iterate until left pointer
    // crosses the right pointer
    while (i < j)
    {
        while (i < j && array[j] == toMove)
 
            // Decrement right pointer
            j--;
 
        if (array[i] == toMove)
 
            // Swap the two elements
            // in the array
            swap(array, i, j);
 
        // Increment left pointer
        i++;
    }
 
    // Return the result
    return array;
}
 
static int[] swap(int []arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    return arr;
}
 
// Driver code
public static void main(String[] args)
{
    int []arr = { 1, 1, 3, 5, 6 };
    int K = 1;
    int []ans = moveElementToEnd(arr, K);
 
    for(int i = 0; i < arr.length; i++)
       System.out.print(ans[i] + " ");
}
}