#include <fstream>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <cmath>

using namespace std; 

int main(){
    
  double delta_x = 0.01;
  double delta_t = 0.5;
  double v_old[101][101];
  double v_new[101][101];
  double r = 2700;
  double k = 200;
  double c = 900;
  double l=2;
  int i;
  double tiempo=0;
  ofstream outfile;

    
    
  for(i=0;i<101;i++){
      if(i>=0 && i<81){
          v_old[i] = 300.0;
	  }
      if(i>119 && i>201){
          v_old[i] = 300.0;
      }
	  else{
          v_old[i] = 500.0;
	}
      }
    while(tiempo<100){
        for(i=0;i<201;i++){
            if(i>0 && i<201){
                v_new[i] = v_old[i]+(delta_t*k/(pow(delta_x, 2)*c*r))*v_old[i+1]+ v_old[i-1]-2*v_old[i][i];
            }
                
             tiempo=tiempo+delta_t;
               }
               
        for(i=1;i<201-1;i++){
            v_old[i] = v_new[i];
      }
        outfile.open("placas.dat");
        for(i=0;i<201;i++){
             outfile << v_old[i] << endl;
    }

  outfile.close();
    
               }

    
return 0;
    
}
