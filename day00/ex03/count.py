# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iwoo <iwoo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 11:35:36 by iwoo              #+#    #+#              #
#    Updated: 2020/04/16 13:51:45 by iwoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import functools
import operator

def text_analyzer(argu_str):

    uppers = string.ascii_uppercase
    lowers = string.ascii_lowercase
    punc_marks = string.punctuation
    print ("The text contains " + str(len(argu_str)) + " characters:")
  #  print ("- " +
   #         str(len(filter((functools.partial(operator.contains, uppers), argu_str)))) +
    #        "upper lettest")
#    print ("- " + count_lower(argu_str) + "lower letters")
 #   print ("- " + "punctuation marks")
  #  print ("- " + "spaces")
