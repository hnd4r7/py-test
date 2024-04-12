import java.util.Scanner;
import java.util.*;
import java.util.stream.Stream;
import java.util.HashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
 
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] files = Arrays.stream(in.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();
 
        Arrays.sort(files);
        int left = 0;
        int right = files.length + 1;
 
        while (left < right){
            int mid = (left + right)/2;
            if(cal(mid, files)){
                right = mid;
            }else {
                left = mid + 1;
            }
        }
        System.out.println(left);
    }
 
    //
    public static boolean cal(int mid, int[] files){
        int[] nums = new int[mid];
        for(int i=0; i<mid; i++){
            nums[i] = 500;
        }
 
        for(int i = files.length - 1; i>=0; i--){
            int f = files[i];
            Arrays.sort(nums);
            if(nums[mid - 1] >= f ){
                nums[mid - 1] -= f;
            }else {
                return false;
            }
        }
 
        return true;
    }
}