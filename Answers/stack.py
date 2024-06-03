class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.size() == 0


    def get_max(self):
        if not self.is_Empty():
            return max(self.items)
        else:
            return None


    def reverse_string(self,input_string):
        for char in input_string:
            self.push(char)

        reversed=""

        while self.size() > 0:
            reversed += self.pop()

        return reversed


    def evaluate_postfix(self, expression):

        operators=set(['+','-','*','/'])

        for token in expression.split():
            if token not in operators:
                self.push(int(token))

            else:
                operand2=self.pop()
                operand1=self.pop()

                if token=='+':
                    result=operand1+operand2
                elif token=='-':
                    result=operand1-operand2
                elif token=='*':
                    result=operand1*operand2
                elif token=='/':
                    result=operand1/operand2
                self.push(result)

        return self.pop()

    def is_balanced(self,expression):

        opening_brackets=set(['(','[','{'])
        closing_brackets=set([')',']','}'])
        bracket_pairs={')':'(',']':'[','}':'{'}

        for char in expression:
            if char in opening_brackets:
                self.push(char)
            elif char in closing_brackets:
                if self.is_Empty() or self.peek() != bracket_pairs[char]:
                    return False
                self.pop()

        return len(self.items)==0


    def prefix_to_postfix(self,expression):

        operators=set(['+','-','*','/'])

        for char in expression[::-1]:
            if char in operators:
                operand1=self.pop()
                operand2=self.pop()
                postfix=operand1+operand2+char
                self.push(postfix)
            else:
                self.push(char)
        return self.pop()

    def infix_to_postfix(self,expression):

        precedence={'+':1,'-':1,'*':2,'/':2}

        postfix=''
        for char in expression:
            if char.isalnum():
                postfix+=char
            elif char == '(':
                self.push(char)
            elif char == ')':
                while not self.is_Empty() and self.peek() != '(':
                    postfix+=self.pop()

                self.pop()

            else:
                while not self.is_Empty() and precedence.get(self.peek(),0) >= precedence[char]:
                    postfix+=self.pop()
                self.push(char)

        while not self.is_Empty():
            postfix+=self.pop()
        return postfix


    def sort_stack(self,stack):

        temp_stack=[]

        while stack:
            temp=stack.pop()
            while not self.is_Empty() and self.peek() > temp:
                temp_stack.append(self.pop())
            self.push(temp)
            while temp_stack:
                self.push(temp_stack.pop())
        return self.items

    def daily_tempareturs(self,tempareturs):

        output=[0]*len(tempareturs)

        for i in range(len(tempareturs)):
            while not self.is_Empty() and tempareturs[i]>tempareturs[self.peek()]:
                prev=self.pop()
                output[prev]=i-prev
            self.push(i)

        return output


    def longest_valid_parentheses(self,expression):
        self.push(-1)
        max_length=0

        for i in range(len(expression)):
            if expression[i]=='(':
                self.push(i)
            else:
                self.pop()
                if self.is_Empty():
                    self.push(i)
                else:
                    max_length = max(max_length,i-self.peek())

        return max_length


