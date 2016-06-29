"""
sage: D=DyckWords(3)
sage: for d in D:
....:     d.pretty_print()
....:
     _
   _|
 _|  .
|  . .

   ___
  | x
 _|  .
|  . .

     _
 ___|
| x  .
|  . .

   ___
 _| x
| x  .
|  . .

 _____
| x x
| x  .
|  . .

sage: D=DyckWords(5)
sage: for i in range(10,15):
    D[i].pretty_print()
....:
         _
   _____|
  | x x  .
  | x  . .
 _|  . . .
|  . . . .

       ___
   ___| x
  | x x  .
  | x  . .
 _|  . . .
|  . . . .

     _____
   _| x x
  | x x  .
  | x  . .
 _|  . . .
|  . . . .

   _______
  | x x x
  | x x  .
  | x  . .
 _|  . . .
|  . . . .

         _
       _|
     _|  .
 ___|  . .
| x  . . .
|  . . . .

sage: for d in DyckWords(3):
    print '\n', ascii_art(d)
....:

/\/\/\

   /\
/\/  \

 /\
/  \/\

 /\/\
/    \

  /\
 /  \
/    \

sage: latex(D[0])
\vcenter{\hbox{$\begin{tikzpicture}[scale=1]
  \draw[dotted] (0, 0) grid (6, 1);
  \draw[rounded corners=1, color=black, line width=2] (0, 0) -- (1, 1) -- (2, 0) -- (3, 1) -- (4, 0) -- (5, 1) -- (6, 0);
\end{tikzpicture}$}}

sage: for d in DyckWords(3):
....:     d.to_triangulation_as_graph().show()

sage: latex(DyckWord([1,0,1,1,0,0]).to_triangulation_as_graph())

sage: d.to_
d.to_132_avoiding_permutation         d.to_noncrossing_permutation
d.to_312_avoiding_permutation         d.to_ordered_tree
d.to_321_avoiding_permutation         d.to_pair_of_standard_tableaux
d.to_Catalan_code                     d.to_partition
d.to_alternating_sign_matrix          d.to_path_string
d.to_area_sequence                    d.to_permutation
d.to_binary_tree                      d.to_standard_tableau
d.to_binary_tree_tamari               d.to_triangulation
d.to_non_decreasing_parking_function  d.to_triangulation_as_graph
d.to_noncrossing_partition

"""