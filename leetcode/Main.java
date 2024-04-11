import java.util.Scanner;
import java.util.*;
import java.util.stream.Stream;
import java.util.HashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
 
public class Main {
    public static int[][] visited;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input_str = in.nextLine();
        String[] tmp2 = input_str.split(" ");
        int[] nums = new int[tmp2.length];
        for (int i = 0; i < tmp2.length; i++) {  
            nums[i] = Integer.parseInt(tmp2[i]);
        }
        int m = nums[0]; 
        int n = nums[1];
        int k = nums[2]; 
 
        visited = new int[m][n];
        System.out.println(dfs(0, 0, m,n,k));
 
    }
 
    public static int dfs(int x, int y, int m, int n, int k) {
        if (x < 0 || y < 0 || x >= m || y >= n) {
            return 0;
        }
        if (visited[x][y]==1) {
            return 0; 
        }
        int total_num = 0;
        int xx = x;
        int yy = y;
        while (xx > 0) {
            total_num += xx % 10; 
            xx /= 10;
        }
 
        while (yy > 0) {
            total_num += yy % 10; 
            yy /= 10;
        }
        if(total_num>k){
            return 0;
        }
 
        visited[x][y] = 1; 
 
        int result = 1;
        if(x+1 <=m){
            result += dfs(x + 1, y, m,n,k);
        }
        if(x-1 >=0){
            result += dfs(x - 1, y, m,n,k);
        }
        if(y+1 <=n){
            result += dfs(x,y+1, m,n,k);
        }
        if(y-1 >=0){
            result += dfs(x, y-1, m,n,k);
        }
 
        return result;
    }
 
}