# step 2: Removing punctuations(full stops,comma,unwanted symbols,etc,..)
# in python there is built in method to find any punctuation in strings that be helpful.
import string
text = "tarun is becoming an ai engineer!!!"
for ch in string.punctuation:
    text = text.replace(ch,"")
print(text) # tarun is becoming an ai engineer
    
    
# these are the all punctuations
"""
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
:
;
<
=
>
?
@
[
\
]
^
_
`
{
|
}
~ """