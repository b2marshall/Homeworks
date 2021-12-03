
member(X,[X|_]).
member(X,[_|T]):-member(X,T).

empty_stack([]).

    % member_stack tests if an element is a member of a stack

member_stack(E, S) :- member(E, S).

    % stack performs the push, pop and peek operations
    % to push an element onto the stack
        % ?- stack(a, [b,c,d], S).
    %    S = [a,b,c,d]
    % To pop an element from the stack
    % ?- stack(Top, Rest, [a,b,c]).
    %    Top = a, Rest = [b,c]
    % To peek at the top element on the stack
    % ?- stack(Top, _, [a,b,c]).
    %    Top = a 

stack(E, S, [E|S]).

%%%%%%%%%%%%%%%%%%%% queue operations %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % These predicates give a simple, list based implementation of 
    % FIFO queues

    % empty queue generates/tests an empty queue


empty_queue([]).

    % member_queue tests if an element is a member of a queue

member_queue(E, S) :- member(E, S).

    % add_to_queue adds a new element to the back of the queue

add_to_queue(E, [], [E]).
add_to_queue(E, [H|T], [H|Tnew]) :- add_to_queue(E, T, Tnew).

    % remove_from_queue removes the next element from the queue
    % Note that it can also be used to examine that element 
    % without removing it
    
remove_from_queue(E, [E|T], T).

append_queue(First, Second, Concatenation) :- 
    append(First, Second, Concatenation).

%%%%%%%%%%%%%%%%%%%% set operations %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % These predicates give a simple, 
    % list based implementation of sets
    
    % empty_set tests/generates an empty set.

empty_set([]).

member_set(E, S) :- member(E, S).

    % add_to_set adds a new member to a set, allowing each element
    % to appear only once

add_to_set(X, S, S) :- member(X, S), !.
add_to_set(X, S, [X|S]).

remove_from_set(_, [], []).
remove_from_set(E, [E|T], T) :- !.
remove_from_set(E, [H|T], [H|T_new]) :-
    remove_from_set(E, T, T_new), !.
    
union([], S, S).
union([H|T], S, S_new) :- 
    union(T, S, S2),
    add_to_set(H, S2, S_new).   
    
intersection([], _, []).
intersection([H|T], S, [H|S_new]) :-
    member_set(H, S),
    intersection(T, S, S_new),!.
intersection([_|T], S, S_new) :-
    intersection(T, S, S_new),!.
    
set_diff([], _, []).
set_diff([H|T], S, T_new) :- 
    member_set(H, S), 
    set_diff(T, S, T_new),!.
set_diff([H|T], S, [H|T_new]) :- 
    set_diff(T, S, T_new), !.

subset([], _).
subset([H|T], S) :- 
    member_set(H, S), 
    subset(T, S).

equal_set(S1, S2) :- 
    subset(S1, S2), subset(S2, S1).
    
%%%%%%%%%%%%%%%%%%%%%%% priority queue operations %%%%%%%%%%%%%%%%%%%

    % These predicates provide a simple list based implementation
    % of a priority queue.
    
    % They assume a definition of precedes for the objects being handled
    
empty_sort_queue([]).

member_sort_queue(E, S) :- member(E, S).

insert_sort_queue(State, [], [State]).  
insert_sort_queue(State, [H | T], [State, H | T]) :- 
    precedes(State, H).
insert_sort_queue(State, [H|T], [H | T_new]) :- 
    insert_sort_queue(State, T, T_new). 
    
remove_sort_queue(First, [First|Rest], Rest).
  


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
  
go2(Start, Goal) :-
	empty_stack(Empty_been_list),
	stack(Start, Empty_been_list, Been_list),
	path(Start, Goal, Been_list).
	
	% path implements a depth first search in PROLOG
	
	% Current state = goal, print out been list
path(Goal, Goal, Been_list) :-
	reverse_print_stack(Been_list).
	
path(State, Goal, Been_list) :-
	move2(State, Next),
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

% Vampires section
unsafe(1,2,0,3,_).
unsafe(1,2,2,1,_).
unsafe(1,2,3,0,_).
unsafe(2,1,0,3,_).
unsafe(2,1,1,2,_).
unsafe(2,1,3,0,_).

%boat on east side of river

move2((0,3,0,3,e), (1,2,0,3,w)) :- not(unsafe(1,2,0,3,w)).
move2((0,3,0,3,e), (0,3,1,2,w)) :- not(unsafe(0,3,1,2,w)).
move2((0,3,0,3,e), (1,2,1,2,w)) :- not(unsafe(1,2,1,2,w)).
move2((0,3,0,3,e), (2,1,0,3,w)) :- not(unsafe(2,1,0,3,w)).
move2((0,3,0,3,e), (0,3,2,1,w)) :- not(unsafe(0,3,2,1,w)).

move2((0,3,1,2,e), (1,2,1,2,w)) :- not(unsafe(1,2,1,2,w)).
move2((0,3,1,2,e), (0,3,2,1,w)) :- not(unsafe(0,3,2,1,w)).
move2((0,3,1,2,e), (1,2,2,1,w)) :- not(unsafe(1,2,2,1,w)).
move2((0,3,1,2,e), (2,1,1,2,w)) :- not(unsafe(2,1,1,2,w)).
move2((0,3,1,2,e), (0,3,3,0,w)) :- not(unsafe(0,3,3,0,w)).

move2((0,3,2,1,e), (1,2,2,1,w)) :- not(unsafe(1,2,2,1,w)).
move2((0,3,2,1,e), (0,3,3,0,w)) :- not(unsafe(0,3,3,0,w)).
move2((0,3,2,1,e), (1,2,3,0,w)) :- not(unsafe(1,2,3,0,w)).
move2((0,3,2,1,e), (2,1,2,1,w)) :- not(unsafe(2,1,2,1,w)). 

move2((0,3,3,0,e), (1,2,3,0,w)) :- not(unsafe(1,2,3,0,w)).
move2((0,3,3,0,e), (2,1,3,0,w)) :- not(unsafe(2,1,3,0,w)).

move2((1,2,0,3,e), (2,1,0,3,w)) :- not(unsafe(2,1,0,3,w)).
move2((1,2,0,3,e), (1,2,1,2,w)) :- not(unsafe(1,2,1,2,w)).
move2((1,2,0,3,e), (2,1,1,2,w)) :- not(unsafe(2,1,1,2,w)).
move2((1,2,0,3,e), (3,0,0,3,w)) :- not(unsafe(3,0,0,3,w)).
move2((1,2,0,3,e), (1,2,2,1,w)) :- not(unsafe(1,2,2,1,w)).

move2((1,2,1,2,e), (2,1,1,2,w)) :- not(unsafe(2,1,1,2,w)).
move2((1,2,1,2,e), (1,2,2,1,w)) :- not(unsafe(1,2,2,1,w)).
move2((1,2,1,2,e), (2,1,2,1,w)) :- not(unsafe(2,1,2,1,w)).
move2((1,2,1,2,e), (3,0,1,2,w)) :- not(unsafe(3,0,1,2,w)).
move2((1,2,1,2,e), (1,2,3,0,w)) :- not(unsafe(1,2,3,0,w)).

move2((1,2,2,1,e), (2,1,2,1,w)) :- not(unsafe(2,1,2,1,w)).
move2((1,2,2,1,e), (1,2,3,0,w)) :- not(unsafe(1,2,3,0,w)).
move2((1,2,2,1,e), (2,1,3,0,w)) :- not(unsafe(2,1,3,0,w)).
move2((1,2,2,1,e), (3,0,2,1,w)) :- not(unsafe(3,0,2,1,w)).

move2((1,2,3,0,e), (2,1,3,0,w)) :- not(unsafe(2,1,3,0,w)).
move2((1,2,3,0,e), (3,0,3,0,w)) :- not(unsafe(3,0,3,0,w)). 

move2((2,1,0,3,e), (3,0,0,3,w)) :- not(unsafe(3,0,0,3,w)).
move2((2,1,0,3,e), (2,1,1,2,w)) :- not(unsafe(2,1,1,2,w)).
move2((2,1,0,3,e), (3,0,1,2,w)) :- not(unsafe(3,0,1,2,w)).
move2((2,1,0,3,e), (2,1,2,1,w)) :- not(unsafe(2,1,2,1,w)).

move2((2,1,1,2,e), (3,0,1,2,w)) :- not(unsafe(3,0,1,2,w)).
move2((2,1,1,2,e), (2,1,2,1,w)) :- not(unsafe(2,1,2,1,w)).
move2((2,1,1,2,e), (3,0,2,1,w)) :- not(unsafe(3,0,2,1,w)).
move2((2,1,1,2,e), (2,1,3,0,w)) :- not(unsafe(2,1,3,0,w)).

move2((2,1,2,1,e), (3,0,2,1,w)) :- not(unsafe(3,0,2,1,w)).
move2((2,1,2,1,e), (2,1,3,0,w)) :- not(unsafe(2,1,3,0,w)).
move2((2,1,2,1,e), (3,0,3,0,w)) :- not(unsafe(3,0,3,0,w)).

move2((2,1,3,0,e), (3,0,3,0,w)) :- not(unsafe(3,0,3,0,w)).

move2((3,0,0,3,e), (3,0,1,2,w)) :- not(unsafe(3,0,1,2,w)).
move2((3,0,0,3,e), (3,0,2,1,w)) :- not(unsafe(3,0,2,1,w)).

move2((3,0,1,2,e), (3,0,2,1,w)) :- not(unsafe(3,0,2,1,w)).
move2((3,0,1,2,e), (3,0,3,0,w)) :- not(unsafe(3,0,3,0,2)).

%boat on west side of river

move2((3,0,3,0,w), (2,1,3,0,e)) :- not(unsafe(2,1,3,0,e)).
move2((3,0,3,0,w), (3,0,2,1,e)) :- not(unsafe(3,0,2,1,e)).
move2((3,0,3,0,w), (2,1,2,1,e)) :- not(unsafe(2,1,2,1,e)).
move2((3,0,3,0,w), (1,2,3,0,e)) :- not(unsafe(1,2,3,0,e)).
move2((3,0,3,0,w), (3,0,1,2,e)) :- not(unsafe(3,0,1,2,e)).

move2((3,0,2,1,w), (2,1,2,1,e)) :- not(unsafe(2,1,2,1,e)).
move2((3,0,2,1,w), (3,0,1,2,e)) :- not(unsafe(3,0,1,2,e)).
move2((3,0,2,1,w), (2,1,1,2,e)) :- not(unsafe(2,1,1,2,e)).
move2((3,0,2,1,w), (1,2,2,1,e)) :- not(unsafe(1,2,2,1,e)).
move2((3,0,2,1,w), (3,0,0,3,e)) :- not(unsafe(3,0,0,3,e)).

move2((3,0,1,2,w), (2,1,1,2,e)) :- not(unsafe(2,1,1,2,e)).
move2((3,0,1,2,w), (3,0,0,3,e)) :- not(unsafe(3,0,0,3,e)).
move2((3,0,1,2,w), (2,1,0,3,e)) :- not(unsafe(2,1,0,3,e)).
move2((3,0,1,2,w), (1,2,1,2,e)) :- not(unsafe(1,2,1,2,e)). 

move2((3,0,0,3,w), (2,1,0,3,e)) :- not(unsafe(2,1,0,3,e)).
move2((3,0,0,3,w), (1,2,0,3,e)) :- not(unsafe(1,2,0,3,e)).

move2((2,1,3,0,w), (1,2,3,0,e)) :- not(unsafe(1,2,3,0,e)).
move2((2,1,3,0,w), (2,1,2,1,e)) :- not(unsafe(2,1,2,1,e)).
move2((2,1,3,0,w), (1,2,2,1,e)) :- not(unsafe(1,2,2,1,e)).
move2((2,1,3,0,w), (0,3,3,0,e)) :- not(unsafe(0,3,3,0,e)).
move2((2,1,3,0,w), (2,1,0,3,e)) :- not(unsafe(2,1,0,3,e)).

move2((2,1,2,1,w), (1,2,2,1,e)) :- not(unsafe(1,2,2,1,e)).
move2((2,1,2,1,w), (2,1,1,2,e)) :- not(unsafe(2,1,1,2,e)).
move2((2,1,2,1,w), (1,2,1,2,e)) :- not(unsafe(1,2,1,2,e)).
move2((2,1,2,1,w), (0,3,2,1,e)) :- not(unsafe(0,3,2,1,e)).
move2((2,1,2,1,w), (2,1,0,3,e)) :- not(unsafe(2,1,0,3,e)).

move2((2,1,1,2,w), (1,2,1,2,e)) :- not(unsafe(1,2,1,2,e)).
move2((2,1,1,2,w), (2,1,0,3,e)) :- not(unsafe(2,1,0,3,e)).
move2((2,1,1,2,w), (1,2,0,3,e)) :- not(unsafe(1,2,0,3,e)).
move2((2,1,1,2,w), (0,3,1,2,e)) :- not(unsafe(0,3,1,2,e)).

move2((2,1,0,3,w), (1,2,0,3,e)) :- not(unsafe(1,2,0,3,e)).
move2((2,1,0,3,w), (0,3,0,3,e)) :- not(unsafe(0,3,0,3,e)). 

move2((1,2,3,0,w), (0,3,3,0,e)) :- not(unsafe(0,3,3,0,e)).
move2((1,2,3,0,w), (1,2,2,1,e)) :- not(unsafe(1,2,2,1,e)).
move2((1,2,3,0,w), (0,3,2,1,e)) :- not(unsafe(0,3,2,1,e)).
move2((1,2,3,0,w), (1,2,1,2,e)) :- not(unsafe(1,2,1,2,e)).

move2((1,2,2,1,w), (0,3,2,1,e)) :- not(unsafe(0,3,2,1,e)).
move2((1,2,2,1,w), (1,2,1,2,e)) :- not(unsafe(1,2,1,2,e)).
move2((1,2,2,1,w), (0,3,1,2,e)) :- not(unsafe(0,3,1,2,e)).
move2((1,2,2,1,w), (1,2,0,3,e)) :- not(unsafe(1,2,0,3,e)).

move2((1,2,1,2,w), (0,3,1,2,e)) :- not(unsafe(0,3,1,2,e)).
move2((1,2,1,2,w), (1,2,0,3,e)) :- not(unsafe(1,2,0,3,e)).
move2((1,2,1,2,w), (0,3,0,3,e)) :- not(unsafe(0,3,0,3,e)).

move2((1,2,0,3,w), (0,3,0,3,e)) :- not(unsafe(0,3,0,3,e)).

move2((0,3,3,0,w), (0,3,2,1,e)) :- not(unsafe(0,3,2,1,e)).
move2((0,3,3,0,w), (0,3,1,2,e)) :- not(unsafe(0,3,1,2,e)).

move2((0,3,2,1,w), (0,3,1,2,e)) :- not(unsafe(3,0,2,1,w)).
move2((0,3,2,1,w), (0,3,0,3,e)) :- not(unsafe(3,0,3,0,2)).




% Sliding puzzle 

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
