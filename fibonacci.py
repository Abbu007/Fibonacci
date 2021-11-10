{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b0e6870e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "x=0\n",
    "y=1\n",
    "z=x+y\n",
    "for i in range(0,n):\n",
    "    z=x+y\n",
    "    x=y\n",
    "    y=z\n",
    "    print(x)\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "319e5ba5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print('p' in 'Python')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "41fe4ef5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_11908/1375745225.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\91818\\AppData\\Local\\Temp/ipykernel_11908/1375745225.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    help(&)\u001b[0m\n\u001b[1;37m         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "help"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "08e30b9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(9//2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1ab7a233",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to expression here. Maybe you meant '==' instead of '='? (Temp/ipykernel_11908/1789377322.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\91818\\AppData\\Local\\Temp/ipykernel_11908/1789377322.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    first-name=\"Tom\"\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m cannot assign to expression here. Maybe you meant '==' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "first-name=\"Tom\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a283c86c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "100/25\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "05f77be8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "9//2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
