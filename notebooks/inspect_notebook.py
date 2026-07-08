import json
with open('01_first_look_and_discovery.ipynb', encoding='utf-8') as f:
    nb = json.load(f)
print('cells', len(nb['cells']))
for i, cell in enumerate(nb['cells']):
    if cell.get('cell_type') == 'markdown':
        src = ''.join(cell.get('source', []))
        print(f'\n===== MARKDOWN CELL {i} =====')
        print(src[:2000])
    elif cell.get('cell_type') == 'code':
        src = ''.join(cell.get('source', []))
        print(f'\n===== CODE CELL {i} =====')
        print(src[:3000])
        if cell.get('outputs'):
            print('---OUTPUTS---')
            for out in cell['outputs']:
                if out.get('output_type') == 'stream':
                    print('STREAM:', ''.join(out.get('text', [])))
                elif out.get('output_type') == 'execute_result':
                    data = out.get('data', {})
                    if 'text/plain' in data:
                        print('RESULT:', ''.join(data['text/plain']))
                elif out.get('output_type') == 'display_data':
                    data = out.get('data', {})
                    if 'text/plain' in data:
                        print('DISPLAY:', ''.join(data['text/plain']))
