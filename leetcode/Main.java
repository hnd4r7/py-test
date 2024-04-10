import java.util.Scanner;
import java.util.*;
import java.util.stream.Stream;
import java.util.HashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
 
public class Main {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input_str = in.nextLine();
        String[] tmp2 = input_str.split(" ");
        int count = 0;
        int[] nums = new int[tmp2.length*2];
        for (int i = 0; i < tmp2.length; i++) {  
            nums[i] = Integer.parseInt(tmp2[i]);
            nums[i+tmp2.length] = Integer.parseInt(tmp2[i]);
            count += 2;
        }
 
        int[] res = new int[count];
        Deque<Integer> stack = new ArrayDeque<Integer>();
        int i=0;
        while(true){
            if(i>=count){
                //没有比它更小的数字的话，那就不赠送寿司，本身就是实际得到寿司的最大价格
                while (!stack.isEmpty()) {
                    int next = stack.pop();
                    res[next] = nums[next];
                }
                String output_str= "";
                //输出一半就行了
                for (int k=0;k<count/2;k++){
                    output_str += res[k] + " ";
                }
                System.out.println(output_str);
                break;
            } else {
                //单调递减栈，套用下面的模板即可
                //https://blog.csdn.net/qq_39445165/article/details/118467075
                while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                    int next = stack.pop();
                    res[next] = nums[next] + nums[i];
                }
                stack.push(i);
            }
            i+=1;
        }
 
    }
}