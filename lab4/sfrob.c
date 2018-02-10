#include<stdio.h>
#include<stdlib.h>

static int frobcmp(const char *a, const char *b)
{
  if(a == NULL || b == NULL)
    {
      fprintf(stderr,"Pointer(s) passed in is invalid!");
      exit(1);
    }
  int i =0;
  while(a[i] != ' ' && b[i] != ' ')
    {
      if((a[i]^42) < (b[i]^42))	
	  return -1;
      else if((a[i]^42) > (b[i]^42))
	  return 1;
      i++;
    }
  
  if(b[i] == a[i])
    return 0;
  if(a[i] == ' ')
    return -1;
  return 1;
}

static int compare(const void* a, const void* b)
{
  return frobcmp(*((const char**)a),*((const char**)b));
}

int main(void)
{
  const int INIT_LEN = 1;
  //record size of array
  int arrSize = 1;
  
  //allocate array of string
  char** arr;
  if(!(arr= (char**)malloc(sizeof(char*))))
    {
      fprintf(stderr,"falied to allocate memory on heap.");
      exit(1);     
    }

  //record size of each string in arr
  int* strSize;
  if(!(strSize = (int*)malloc(sizeof(int))))
    {
      fprintf(stderr,"falied to allocate memory on heap.");
      exit(1);     
    }
     
  if(!(arr[0]= (char*)malloc(INIT_LEN)))
    {
      fprintf(stderr,"falied to allocate memory on heap.");
      exit(1);
    }

  strSize[0] = INIT_LEN;

  int indexOfStr = 0; 
  int num = 0;//index for each char
  char buffer = getchar();

  //check input error
  if(ferror(stdin))
    {
      fprintf(stderr,"falied to read from input.");
      exit(1);
    }

  while(buffer != EOF)
   {
     //if string length exceeds the given length, increase the length
     if(num >= strSize[indexOfStr])
       {
	 strSize[indexOfStr]++;
	 if(!(arr[indexOfStr] = (char*)realloc(arr[indexOfStr],strSize[indexOfStr])))
	   {
	     fprintf(stderr,"falied to allocate memory on heap.");
	     exit(1);     
	   }
       }
     arr[indexOfStr][num] = buffer;
     num++;

     //if the char read is a space
     if(buffer == ' ')
       {
	 //switch to next string
         indexOfStr++;
	 arrSize++;
	 //record length for the new string
	 if(!(strSize = (int*)realloc(strSize,arrSize * sizeof(int))))
	   {
	     fprintf(stderr,"falied to allocate memory on heap.");
	     exit(1);     
	   }
	 strSize[indexOfStr] = INIT_LEN;
	 
	 //increase the length of arr
	 if(!(arr = (char**)realloc(arr,arrSize * sizeof(char*))))
	   {
	     fprintf(stderr,"falied to allocate memory on heap.");
	     exit(1);     
	   }
	     
	 //allocate space for new string
	 if(!(arr[indexOfStr] = (char*)malloc(INIT_LEN)))
	   {
	     fprintf(stderr,"falied to allocate memory on heap.");
	     exit(1);     
	   }
	  
	 num = 0;	 
       }
     buffer = getchar();
     if(ferror(stdin))
       {
	 fprintf(stderr,"falied to read from input.");
	 exit(1);
       }
   }

 //if the input end with space, free the last entry in the array(which is empty)
 if(num == 0)
   {
     free(arr[indexOfStr]);
     arrSize--;
     indexOfStr--;
   }
 //else append a space to the last entry 
 else
   {
     if(num >= strSize[indexOfStr])
       {
	 strSize[indexOfStr]++;
	 if(!(arr[indexOfStr] = (char*)realloc(arr[indexOfStr],strSize[indexOfStr])))
	   {
	     fprintf(stderr,"falied to allocate memory on heap.");
	     exit(1);     
	   }
       }
     arr[indexOfStr][num] = ' ';
   }

 qsort(arr,arrSize,sizeof(char*),compare);  

 int i,j;
 for(i = 0;i < arrSize;i++)
   {
     j = 0;
     while(arr[i][j] != ' ')
       {
	 putchar(arr[i][j]);

	 //error checking for output
	 if(ferror(stdout))
	   {
	     fprintf(stderr,"failed to output data.");
	     exit(1);
	   }
	 j++;
       }
     putchar(' ');
     //error checking for output
     if(ferror(stdout))
       {
	 fprintf(stderr,"failed to output data.");
	 exit(1);
       }
     
   }

 //free all allocated memory
 for(i = 0; i < arrSize;i++)
     free(arr[i]);
 free(strSize);
 free(arr);
 return 0;
}
