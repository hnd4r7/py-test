import java.util.Scanner;
import java.util.*;
import java.util.stream.Stream;
import java.util.HashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
 
public class Main {
    
    public static void main(String[] args) {
        //输入
        Scanner in = new Scanner(System.in);
        //处理输入
        int n = in.nextInt();
        int[][] matrix = new int[n][3];
        for (int i = 0; i < n; i++) {
            matrix[i][0] = in.nextInt();
            matrix[i][1] = in.nextInt();
            matrix[i][2] = in.nextInt();
        }
 
        HashMap<Integer, Integer> relation = new HashMap<>();
        Arrays.sort(matrix, (a, b) -> b[1] - a[1]);
    
        int top = matrix[matrix.length - 1][1];
    
        for (int[] current_layer : matrix) {
            int id = current_layer[0];
            int up_id = current_layer[1];
            int money = current_layer[2];
        
            if (relation.containsKey(id)) {
                money += relation.get(id);
            }
            relation.put(up_id, relation.getOrDefault(up_id, 0) + money / 100 * 15);
        }
    
        System.out.println(top + " " + relation.get(top));
    }
    
}