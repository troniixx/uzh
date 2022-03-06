/****************************************************************************
 * University of Zurich, Informatics II, Spring Semester 2022               *
 * Exercise 2 - Task 3                                                      *
 *                                                                          *
 * @author Mert Erol                                                        *
 ****************************************************************************/

#include <stdio.h>

// TODO: your implementation
int blink_me_daddy(int blinks) {
	if(blinks == 1){
		return 1; } 
			else if(blinks == 2){return 2; } 
				else {
					return blink_me_daddy(blinks - 1)+(blinks-2);
		
	//num of blinks == blinks.previous+(blinks-2)

	}


}

int main() {
	int input;
	printf("Enter the number of blinks: ");
	scanf("%d", &input);

	// TODO: your implementation
	printf("%d", blink_me_daddy(input));

	return 0;
}
