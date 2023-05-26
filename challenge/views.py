from django.shortcuts import render
from challenge.scripts.CodeTreeADT import CodeTreeADT


def convert(request):
    context = {}

    if request.method == 'POST':
        codification = request.POST.get('codification')
        action = request.POST.get('action')
        message = request.POST.get('message')

        print(codification)
        print(action)
        print(message)


        if action == 'encode':
            if codification == 'binary':
                binary_tree = CodeTreeADT(binary=True)
                context['translation'] = binary_tree.encode(message)
            elif codification == 'morse':
                morse_tree = CodeTreeADT(morse=True)
                context['translation'] = morse_tree.encode(message)
            else:
                context['translation'] = "Error"
        elif action == 'decode':
            if codification == 'binary':
                binary_tree = CodeTreeADT(binary=True)
                context['translation'] = binary_tree.decode(message)
            elif codification == 'morse':
                morse_tree = CodeTreeADT(morse=True)
                context['translation'] = morse_tree.decode(message)
            else:
                context['translation'] = "Error"
        else:
            context['translation'] = "Error"

    return render(request, 'subtemplates/conversor.html', context)
