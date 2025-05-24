# HASS
## Q&A
- What is it?  
The project came from [HASS](https://github.com/HArmonizedSS/HASS) and was modified by IamMI.  
- Why do you do it?  
I want to replcate the project.  

## Modify
### 1. `model.cnets_hass.LlamaAttention.forward`  

Original version:  
```
total_attn_weights = nn.functional.softmax(total_attn_weights, dim=-1, dtype=torch.float32 ).to(query_states.dtype) 
```  
Modified version:  
```
total_attn_weights = nn.functional.softmax(total_attn_weights+attention_mask, dim=-1, dtype=torch.float32 ).to(query_states.dtype) 
```
