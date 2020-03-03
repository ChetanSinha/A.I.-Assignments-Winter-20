# 8 Queens Problem implementation using A Star Algorithm #
## State space: ##
*  Here state space is a 8x8 matrix where the position of a queen is represented by 1
## State transition operator: ##
* Adding a new queen which is denoted by 1 in the subsequent row.
## Intitial state: ##
* A 8 x 8 null matrix.
## Goal state: ##
* When all the rows are filled with a single queen at non attacking positions,
## Cost: ## 
* Heuristic cost decreases with the number of queens.
* Path cost increases with the number of queens.
* The total cost i got with my approach was 803.
