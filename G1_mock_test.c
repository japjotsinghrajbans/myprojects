/*
    author: Japjot Singh Rajbans
    date: August 8, 2026
    title: G1 Mock Test (in C!)
*/

#include <stdio.h>

// The test
void theTest() {
    char A1;
    char A2;
    char A3;
    char A4;
    char A5;
    char A6;
    char A7;
    char A8;
    char A9;
    char A10;
    char A11;
    char A12;
    char A13;
    char A14;
    char A15;
    int numScore = 0;

    // Question 1
    printf("Q1) If a fully licensed driver is convicted of using a hand-held electronic device while driving, they will face which of the following penalties for a first offence?\na) A fine of up to $1,000 and 3 demerit points\nb) A fine of up to $500 and 2 demerit points\nc) A 30-day licence suspension\nd) None of the above\nAnswer: ");
    scanf(" %c", &A1);
    if (A1 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) A fine of up to $1,000 and 3 demerit points.\nYour live score is now: %d\n", numScore);
    }

    // Question 2
    printf("Q2) You will receive _____ the first time you are convicted of a Criminal Code offence.\na) a one-year licence suspension\nb) a lifetime ban from driving\nc) a one-month licence suspension\nd) a two-year licence suspension\nAnswer: ");
    scanf(" %c", &A2);
    if (A2 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct is...\na) a one-year licence suspension.\nYour live score is now: %d\n", numScore);
    }

    // Question 3
    printf("Q3) Under Ontario's Move Over law, you are required to...\na) pull over if an emergency vehicle is following you with its lights flashing.\nb) change lanes if safe when passing a stopped emergency vehicle with its lights flashing\nc) move into the rightmost lane if you are driving slower than other traffic.\nd) do none of the above.\nAnswer: ");
    scanf(" %c", &A3);
    if (A3 == 'b') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! Your live score is now: %d\n", numScore);
    }

    // Question 4
    printf("Q4) Do NOT park anywhere that you don't have a clear view for at least ___ metres in both directions.\na) 125\nb) 135\nc) 150\nd) 175\nAnswer: ");
    scanf(" %c", &A4);
    if (A4 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) 125\nYour live score is now: %d\n", numScore);
    }

    // Question 5
    printf("Q5) You may NOT park within ________ of an intersection that is NOT controlled by traffic lights.\na) 5 metres\nb) 7 metres\nc) 9 metres\nd) 15 metres\nAnswer: ");
    scanf(" %c", &A5);
    if (A5 == 'c') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\nc) 9 metres\nYour live score is now: %d\n", numScore);
    }

    // Question 6
    printf("Q6) While driving, a Class G1 learner must be supervised by an accompanying driver. The blood-alcohol level of the accompanying driver must be less than...\na) 0.02%\nb) 0.05%\nc) 0.07%\nd) 0.08%\nAnswer: ");
    scanf(" %c", &A6);
    if (A6 == 'b') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\nb) 0.05%\nYour live score is now: %d\n", numScore);
    }

    // Question 7
    printf("Q7) If you are found guilty of backing on a highway or driving too slowly, _ demerit points will be added to your driving record.\na) 5\nb) 3\nc) 2\nd) 1\nAnswer: ");
    scanf(" %c", &A7);
    if (A7 == 'c') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\nc) 2\nYour live score is now: %d\n", numScore);
    }

    // Question 8
    printf("Q8) A G2 driver age 19 or younger who has 6 months or less of driving experience may carry _ unrelated passenger(s) age 19 or younger between midnight and 5 AM.\na) 1\nb) 2\nc) 3\nd) 4\nAnswer: ");
    scanf(" %c", &A8);
    if (A8 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) 1\nYour live score is now: %d\n", numScore);
    }

    // Question 9
    printf("Q9) If you are convicted of following too closely (tailgating), _ demerit points will be added to your driving record.\na) 4\nb) 5\nc) 2\nd) 6\nAnswer: ");
    scanf(" %c", &A9);
    if (A9 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) 4\nYour live score is now: %d\n", numScore);
    }

    // Question 10
    printf("Q10) What does the sign with an orange background and an arrow pointing at top left mean?\na) Closed lane\nb) Road turns left\nc) Slight bend or curve in the road ahead\nd) Yield to the left\nAnswer: ");
    scanf(" %c", &A10);
    if (A10 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) Closed lane\nYour live score is now: %d\n", numScore);
    }

    // Question 11
    printf("Q11) A G2 driver age 19 or younger who has more than 6 months of driving experience may carry _ unrelated passenger(s) age 19 or younger between midnight and 5 AM.\na) 1\nb) 2\nc) 3\nd) 4\nAnswer: ");
    scanf(" %c", &A11);
    if (A11 == 'c') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\nc) 3\nYour live score is now: %d\n", numScore);
    }

    // Question 12
    printf("Q12) If you are convicted for the first time of driving while your licence is suspended, you will get an additional six-month suspension, and you will also face which of the following additional penalties?\na) A fine of between $1,000 and $5,000\nb) Either jail time or a fine or both\nc) Six months in jail\nd) Neither jail time nor a fine\nAnswer: ");
    scanf(" %c", &A12);
    if (A12 == 'b') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\nb) Either jail time or a fine or both\nYour live score is now: %d\n", numScore);
    }

    // Question 13
    printf("Q13) What does the sign with a thick road strip on the left and 'Do not cross' written on the right mean?\na) Vehicles cannot change lanes into or out of a high-occupancy vehicle (HOV) lane in this area.\nb) There is a railway crossing ahead. Be alert for trains.\nc) There is a hazard close to the edge of the road. The downward lines show the side on which you may safely pass.\nd) There is a pedestrian crossover. Be prepared to stop and yield te right-of-way to pedestrians.\nAnswer: ");
    scanf(" %c", &A13);
    if (A13 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) Vehicles cannot change lanes into or out of a high-occupancy vehicle (HOV) lane in this area.\nYour live score is now: %d\n", numScore);
    }

    // Question 14
    printf("Q14) If you are found guilty of going the wrong way on a one-way road, _ demerit points will be added to your driving record.\na) 2\nb) 5\nc) 6\nd) 3\nAnswer: ");
    scanf(" %c", &A14);
    if (A14 == 'd') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\nd) 3\nYour live score is now: %d\n", numScore);
    }

    // Question 15
    printf("Q15) If you are found guilty of carrying a child passenger who is not properly secured, _ demerit points will be added to your driving record.\na) 2\nb) zero\nc) 4\nd) 3\nAnswer: ");
    scanf(" %c", &A15);
    if (A15 == 'a') {
        numScore += 1;
        printf(">>> That's correct! Your live score is now: %d\n", numScore);
    }
    else {
        printf(">>> Unfortunately, that's not right! The correct answer is...\na) 2\nYour live score is now: %d\n", numScore);
    }

    // Final Result
    float percentage = ((float) numScore / 15) * 100;
    printf("-----------------------------------------\n");
    printf(">>> Your total score is: %d/15\n", numScore);
    printf(">>> Your percentage is: %.2f%%\n", percentage);
    if (percentage >= 80.0) {
        printf(">>> Congratulations! You have passed the G1 Mock Test! I know you will do well in the real test! :D");
    }
    else {
        printf(">>> Oh well, better luck next time! :/");
    }
}

// Main
int main() {
    char placeholder;
    // Introduction
    printf("--------------------------------------------\n");
    printf("Welcome to the G1 Ontario Mock Test made by Japjot!\n");
    printf("Each question is worth 1 mark.\n");
    printf("These are MCQs covering various topics like road signs, traffic laws, and safe driving practices.\n");
    printf("Remember: stay calm, answer wisely, and all the best! :)\n");
    printf("--------------------------------------------\n");
    printf("Press any visible key, then press Enter to begin this mock test...\n");
    printf("--------------------------------------------\n");
    scanf(" %c", &placeholder);
    if (placeholder != ' ') {
        theTest();
    }
    return 0;
}
