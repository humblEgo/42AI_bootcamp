# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iwoo <iwoo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/15 22:18:33 by iwoo              #+#    #+#              #
#    Updated: 2020/04/15 22:51:23 by iwoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2:
    sys.exit("Error")
else:
    try:
        num = int(sys.argv[1])
    except:
        sys.exit("Error")

if (num == 0):
    print ("I'm Zero.")
elif (num % 2 == 0):
    print ("I'm Even.")
else:
    print ("I'm Odd.")
