package Noah_Peterson_HW6;
import java.util.*;


public class ScheduleGreedy {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		System.out.println("How many jobs would you like to schedule?");
		int size = keyboard.nextInt();
		int[] jobs = new int[size];
		for(int i = 0; i < size; i++) {
			System.out.println("Please enter the time for job " + (i+1) + ".");
			jobs[i] = keyboard.nextInt();
		}
		keyboard.close();
		
		
		printArray(scheduleIt(jobs));
		
	}

    public static void Finish(int[][] oupt, int i, int[] []ar1, int i1){
        while(i1 < ar1.length && i < oupt.length){
            oupt[i] = ar1[i1];
            i1 ++;
            i ++;
            
        }

    }



    public static int[][] Merge(int[][] ar1, int[][] ar2)
	{
        int oupt[][];
        oupt = new int[ar1.length + ar2.length][];
        int i=-1 ;
        int i1=0 ;
        int i2=0 ;
        for(i ++ ; i < oupt.length; i++){
            if(i1 >= ar1.length){
                Finish(oupt, i, ar2, i2);
                break;
            }
            else if(i2 >= ar2.length){
                Finish(oupt, i, ar1, i1);
                break;
            }
            else{
                if(ar1[i1][0] <= ar2[i2][0]){
                    oupt[i] = ar1[i1];
                    i1 ++;
                }
                else{
                    oupt[i] = ar2[i2];
                    i2 ++;
                }
            }
            
        }
        return(oupt);
	}
    public static int[][] subArray(int[][] arr, int a, int b)
	{   
        int oupt1[][];
        oupt1 = new int[b-a][];
        for(int i = 0; i < b-a ; i++){
            oupt1[i] = arr[i+a];
        }
        return(oupt1);
    }

	public static int[][] scheduleIt1(int[][] jobs)
	{

        if(jobs.length == 1){
            return(jobs);
        }
        else{
            int mid = (int) Math.floor(jobs.length/2);

            return(Merge(scheduleIt1(subArray(jobs,0,mid)), scheduleIt1(subArray(jobs,mid, jobs.length))));
        }
	}
    public static int[] scheduleIt(int[] jobs){
        int[][] jobs2 = new int[jobs.length][];
        for(int i = 0; i < jobs.length; i++){
            jobs2[i] = new int[]{jobs[i],i};
        }
        int[] oupt = new int[jobs.length];
        int[][] oupt1 = scheduleIt1(jobs2);
        for(int i = 0; i < jobs.length; i++){
            oupt[i] = oupt1[i][1];
        }
        return(oupt);


    }
	
	private static void printArray(int[] arr) {
        System.out.print("[");
		for(int i = 0; i < arr.length-1; i++)
			System.out.print((arr[i]+1) + ", ");
		System.out.print(arr[arr.length-1]+1);
        System.out.println("]");
	}
}
