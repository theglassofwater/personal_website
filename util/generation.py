import torch
from transformers import GenerationConfig

def generate_comparison_song(model, tokenizer, ids, max_length):
    model.eval()
    new_tokens = max_length - len(ids)

    input = torch.tensor([ids])
    # input = torch.tensor([[1,]]) # bar_none, position_0
    # input = ids

    generation_config = GenerationConfig(
        max_new_tokens=new_tokens,
        min_tokens=25,
        do_sample=True,
        temperature=0.9,
        pad_token_id=tokenizer.pad_token_id,
    )
    if torch.cuda.is_available():
        input = input.cuda()

    output = model.generate(input, generation_config=generation_config)
    return output[0]
