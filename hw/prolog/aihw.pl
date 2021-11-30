go(Start, Goal) :-
	empty_stack(Empty_been_list),
	stack(Start, Empty_been_list, Been_list),
	path(Start, Goal, Been_list).
	
	% path implements a depth first search in PROLOG
	
	% Current state = goal, print out been list
path(Goal, Goal, Been_list) :-
	reverse_print_stack(Been_list).
	
path(State, Goal, Been_list) :-
	move(State, Next),
	% not(unsafe(Next)),
	not(member_stack(Next, Been_list)),
	stack(Next, Been_list, New_been_list),
	path(Next, Goal, New_been_list), !.
	
reverse_print_stack(S) :-
	empty_stack(S).
reverse_print_stack(S) :-
	stack(E, Rest, S),
	reverse_print_stack(Rest),
	write(E), nl.
  


move([0, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P],  [B, 0, C, D, E, F, G, H, I, J, K, L, M, N, O, P]).
move([0, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P],  [E, B, C, D, 0, F, G, H, I, J, K, L, M, N, O, P]). 
move([A, 0, C, D, E, F, G, H, I, J, K, L, M, N, O, P],  [0, A, C, D, E, F, G, H, I, J, K, L, M, N, O, P]).
move([A, 0, C, D, E, F, G, H, I, J, K, L, M, N, O, P],  [A, C, 0, D, E, F, G, H, I, J, K, L, M, N, O, P]).
move([A, 0, C, D, E, F, G, H, I, J, K, L, M, N, O, P],  [A, F, C, D, E, 0, G, H, I, J, K, L, M, N, O, P]).
move([A, B, 0, D, E, F, G, H, I, J, K, L, M, N, O, P],  [A, 0, B, D, E, F, G, H, I, J, K, L, M, N, O, P]).
move([A, B, 0, D, E, F, G, H, I, J, K, L, M, N, O, P],  [A, B, D, 0, E, F, G, H, I, J, K, L, M, N, O, P]).
move([A, B, 0, D, E, F, G, H, I, J, K, L, M, N, O, P],  [A, B, G, D, E, F, 0, H, I, J, K, L, M, N, O, P]).
move([A, B, C, 0, E, F, G, H, I, J, K, L, M, N, O, P],  [A, B, 0, C, E, F, G, H, I, J, K, L, M, N, O, P]).
move([A, B, C, 0, E, F, G, H, I, J, K, L, M, N, O, P],  [A, B, C, E, 0, F, G, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, 0, F, G, H, I, J, K, L, M, N, O, P],  [A, B, C, 0, D, F, G, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, 0, F, G, H, I, J, K, L, M, N, O, P],  [A, B, C, D, F, 0, G, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, 0, F, G, H, I, J, K, L, M, N, O, P],  [A, B, C, D, I, F, G, H, 0, J, K, L, M, N, O, P]).
move([A, B, C, D, E, 0, G, H, I, J, K, L, M, N, O, P], [A, 0, C, D, E, B, G, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, 0, G, H, I, J, K, L, M, N, O, P], [A, B, C, D, 0, E, G, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, 0, G, H, I, J, K, L, M, N, O, P], [A, B, C, D, E, G, 0, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, 0, G, H, I, J, K, L, M, N, O, P], [A, B, C, D, E, J, G, H, I, 0, K, L, M, N, O, P]).
move([A, B, C, D, E, F, 0, H, I, J, K, L, M, N, O, P],  [A, B, 0, D, E, F, C, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, F, 0, H, I, J, K, L, M, N, O, P],  [A, B, C, D, E, 0, F, H, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, F, 0, H, I, J, K, L, M, N, O, P],  [A, B, C, D, E, F, H, 0, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, F, 0, H, I, J, K, L, M, N, O, P],  [A, B, C, D, E, F, K, H, I, J, 0, L, M, N, O, P]).
move([A, B, C, D, E, F, G, 0, I, J, K, L, M, N, O, P],  [A, B, C, 0, E, F, G, D, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, F, G, 0, I, J, K, L, M, N, O, P],  [A, B, C, D, E, F, 0, G, I, J, K, L, M, N, O, P]).
move([A, B, C, D, E, F, G, 0, I, J, K, L, M, N, O, P],  [A, B, C, D, E, F, G, L, I, J, K, 0, M, N, O, P]).
move([A, B, C, D, E, F, G, H, 0, J, K, L, M, N, O, P], [A, B, C, D, 0, F, G, H, E, J, K, L, M, N, O,P]).
move([A, B, C, D, E, F, G, H, 0, J, K, L, M, N, O, P],  [A, B, C, D, E, F, G, H, J, 0, K, L, M, N, O, P]).
move([A, B, C, D, E, F, G, H, 0, J, K, L, M, N, O, P],  [A, B, C, D, E, F, G, H, M, J, K, L, 0, N, O, P]).
move([A, B, C, D, E, F, G, H, I, 0, K, L, M, N, O, P], [A, B, C, D, E, 0, G, H, I, F, K, L, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, 0, K, L, M, N, O, P], [A, B, C, D, E, F, G, H, 0, I, K, L, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, 0, K, L, M, N, O, P], [A, B, C, D, E, F, G, H, I, K, 0, L, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, 0, K, L, M, N, O, P], [A, B, C, D, E, F, G, H, I, N, K, L, M, 0, O, P]).
move([A, B, C, D, E, F, G, H, I, J, 0, L, M, N, O, P], [A, B, C, D, E, F, 0, H, I, J, G, L, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, J, 0, L, M, N, O, P], [A, B, C, D, E, F, G, H, I, 0, J, L, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, J, 0, L, M, N, O, P], [A, B, C, D, E, F, G, H, I, J, L, 0, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, J, 0, L, M, N, O, P], [A, B, C, D, E, F, G, H, I, J, O, L, M, N, 0, P]).
move([A, B, C, D, E, F, G, H, I, J, K, 0, M, N, O, P], [A, B, C, D, E, F, G, 0, I, J, K, H, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, J, K, 0, M, N, O, P], [A, B, C, D, E, F, G, H, I, J, 0, K, M, N, O, P]).
move([A, B, C, D, E, F, G, H, I, J, K, 0, M, N, O, P], [A, B, C, D, E, F, G, H, I, J, K, P, M, N, O, 0]).
move([A, B, C, D, E, F, G, H, I, J, K, L, 0, N, O, P], [A, B, C, D, E, F, G, H, 0, J, K, L, I, N, O, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, 0, N, O, P], [A, B, C, D, E, F, G, H, I, J, K, L, N, 0, O, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, 0, O, P], [A, B, C, D, E, F, G, H, I, 0, K, L, M, J, O, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, 0, O, P], [A, B, C, D, E, F, G, H, I, J, K, L, 0, M, O, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, 0, O, P], [A, B, C, D, E, F, G, H, I, J, K, L, M, O, 0, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, N, 0, P], [A, B, C, D, E, F, G, H, I, J, 0, L, M, N, K, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, N, 0, P], [A, B, C, D, E, F, G, H, I, J, K, L, M, 0, N, P]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, N, 0, P], [A, B, C, D, E, F, G, H, I, J, K, L, M, N, P, 0]). 
move([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, 0],  [A, B, C, D, E, F, G, H, I, J, K, 0, M, N, O, L]).
move([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, 0],  [A, B, C, D, E, F, G, H, I, J, K, L, M, N, 0, O]).
