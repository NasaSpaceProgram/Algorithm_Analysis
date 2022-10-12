// The method scheduleIt is a greedy algorithm for scheduling jobs.

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int* scheduleIt(int size, int* jobs);
void printArray(int size, int* arr);
void Finish(int* oupt, int i, int* ar1, int i1);

int main()
{
	int size;
	cout << "How many jobs would you like to schedule?" << endl;
	cin >> size;
	int* jobs = new int[size];
	for(int i = 0; i < size; i++){
		cout << "Please enter the time for job " << i + 1 << "." << endl;
		cin >> jobs[i];
	}
	cout << "[";
	printArray(size, scheduleIt(size, jobs));
	cout << "]" << endl;

}

void Finish(int* oupt, int i, int* ar1, int i1){
        while(i1 < sizeof(ar1) && i < sizeof(oupt)){
            oupt[i] = ar1[i1];
            i ++;
            i1 ++;
        }

    }



int* Merge(int* ar1, int* ar2)
	{
        int oupt[sizeof(ar1) + sizeof(ar2)];
        int i=-1 ;
        int i1=0 ;
        int i2=0 ;
        for(i ++ ; i < sizeof(oupt); i++){
            if(i1 >= sizeof(ar1)){
                Finish(oupt, i, ar2, i2);
            }
            else if(i2 >= sizeof(ar2)){
                Finish(oupt, i, ar1, i1);
            }
            else{
                if(ar1[i1] <= ar2[i2]){
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

int* subArr(int* arr, int a, int b){
    int oupt1[b-a];
    for(int i = 0; i < b-a - 1; i++){
        oupt1[i] = arr[i+a];
    }
    return(oupt1);
}

static int* scheduleIt(int* jobs)
	{
        if(sizeof(jobs) == 1){
            return(jobs);
        }
        else{
            int mid = (int) floor(sizeof(jobs)/2);
            return(Merge(scheduleIt(subArr(jobs, 0, mid)), scheduleIt(subArr(jobs, mid, sizeof(jobs)))));
        }
	}

void printArray(int size, int* arr){
	for(int i = 0; i < size - 1; i++)
		cout << (arr[i] + 1) << ", ";
	cout << (arr[size-1]) + 1;
}