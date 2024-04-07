import java.util.Scanner;
import java.util.*;
import java.util.stream.Collectors;
 
public class Main { 
    public static void main(String[] args) {
        //处理输入
        Scanner in=new Scanner(System.in); 
        String input_str = in.nextLine();
        String[] tmp2 = input_str.split(" ");
        int[][] jobs = new int[tmp2.length/2][2];
        for (int i = 0; i < tmp2.length; i+=2) {  
            //提交时间
            jobs[i/2][0] = Integer.parseInt(tmp2[i]);
            //执行时间
            jobs[i/2][1] = Integer.parseInt(tmp2[i+1]);
        }
        //按照提交时间排序
        Arrays.sort(jobs,(a,b)->a[0]-b[0]);
        
 
        String[] tmp1 = in.nextLine().split(" ");
        int[] params = new int[tmp1.length];
        for (int i = 0; i < tmp1.length; i++) {  
            params[i] = Integer.parseInt(tmp1[i]);
        }
        int max_q_len = params[0];
        int max_workers = params[1];
 
        LinkedList<Integer> queue = new LinkedList();
        int[] workers = new int[max_workers];
        int total_time = 0;
        //丢弃个数
        int droped = 0;
 
        int i = 0;
        while(true){
            if(i>=jobs.length){
                break;
            } else {
                // 当前执行者是否有空闲？
                int idle_worker = -1;
                for(int j=0;j<max_workers;j++){
                    //正在执行者时间减1
                    if(workers[j]!=0){
                        workers[j]-=1;
                    }
                    //优先级最高的空闲执行者
                    if (workers[j]==0 && idle_worker ==-1){
                        idle_worker = j;
                    }
                    
                }
 
                // 若有空闲执行者，则赋给空闲执行者
                if(idle_worker!=-1){
                    if(queue.size()>0) {
                        workers[idle_worker] = queue.removeFirst();  
                    } 
                } 
 
                //此刻是否有提交的任务
                if(total_time == jobs[i][0]){
                    if(queue.size()>=max_q_len){
                        //丢弃
                        queue.removeFirst();  
                        queue.addLast(jobs[i][1]);
                        droped += 1;
                    } else{
                        queue.addLast(jobs[i][1]);
                    }
                    i+=1;
                } 
 
                // 应对特殊情况
                if(idle_worker!=-1){
                    if(queue.size()>0) {
                        workers[idle_worker] = queue.removeFirst();  
                    } 
                } 
                
                total_time += 1;
            }
            
        }
 
        System.out.print(total_time + jobs[i-1][1]);
        System.out.print(" ");
        System.out.print(droped);
    }
    
}