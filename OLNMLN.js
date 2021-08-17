function run(code='wCode autwofilled.',console_output_q=false){
    function resetout(){
        if(console_output_q==true){console.log('\n-----\nCONSOLE RESET\n-----\n')}else{document.getElementById('out').innerHTML=''}
    }
    function out(val){
        if(console_output_q==true){
            console.log(val)
        }else{
            document.getElementById('out').innerHTML+=val
        }
    }
    resetout()
    let i=0
    let char=code[i]
    let STACK=[]
    while(char!='s'&&i<code.length){
        let output=''
        if(char=='\u02C7'){
            i++
            if(code[i]=='{'){STACK.push('\n')}
            else if(code[i]=='}'){STACK.push('\t')}
            else{STACK.push(code[i])}
        }else if(char=='p'){
            chars=''
            for(let _=0;_<4;_++){
                i++
                chars+=code[i]
            }
            STACK.push(parseFloat(chars))
        }else if(char=='i'){
            STACK.reverse()
        }else if(char=='c'){
            STACK.push(STACK[-1])
        }else if(char=='+'){
            n1=STACK.pop()
            n2=STACK.pop()
            STACK.push(n1+n2)
        }else if(char=='-'){
            n1=STACK.pop()
            n2=STACK.pop()
            STACK.push(n1-n2)
        }else if(char=='*'){
            n1=STACK.pop()
            n2=STACK.pop()
            STACK.push(n1*n2)
        }else if(char=='/'){
            n1=STACK.pop()
            n2=STACK.pop()
            STACK.push(n1/n2)
        }else if(char=='%'){
            n1=STACK.pop()
            n2=STACK.pop()
            STACK.push(n1%n2)
        }else if(char=='^'){
            output+=STACK.pop()
        }else if(char=='r'){
            STACK.pop()
        }else if(char=='d'){
            n=STACK.pop()
            if(n<=0&&isNaN(n)!=true){i++}
        }else if(char=='n'){
            n=STACK.pop()
            i+=n
        }else if(char=='>'){
            STACK.push(prompt('Input for script'))
        }else if(char=='$'){n=prompt('Input for script')
            if(parseFloat(n)!=undefined){STACK.push(parseFloat(n))}else{STACK.push(n)}
        }else if(char=='w'){
            chars=''
            for(let _=0;_<8;_++){
                i++
                chars+=code[i]
            }output+=chars
        }else if(char=='j'){
            chars=''
            for(let _=0;_<4;_++){
                i++
                chars+=code[i]
            }i+=parseFloat(chars)-5
        }
        out(output)
        i++
        char=code[i]
    }
}