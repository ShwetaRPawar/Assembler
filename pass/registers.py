assign={'eax':'reg1','ecx':'reg2','edx':'reg3','ebx':'reg4','esi':'reg5','edi':'reg6','esp':'reg7','ebp':'reg8'}
inst=['mov','add','sub','mul','div','xor','jmp','jnz','jz','printf','scanf','pusha','popa','push','pop','call','inc','dec','cmp','jnz','jle','jge']
sections=['section','global','extern','.data','.text','.bss','main','printf','scanf','printf,scanf']
reg=['eax','ecx','edx','ebx','esi','edi','esp','ebp']

err=[]
err_line=[]
err_name=[]
err_spec=[]
mac_name=[]
mac_para=[]
mac_def=[] 
