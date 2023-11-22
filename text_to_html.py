# Ouvrir le fichier source en mode lecture
with open('article1.txt', 'r') as src_file:
  # Ouvrir le fichier de destination en mode écriture
  with open('destination.html', 'w') as dest_file:
    in_list = False  # Indicateur pour savoir si nous sommes à l'intérieur d'une liste
    first_line = True  # Indicateur pour savoir si nous sommes à la première ligne
    # Lire chaque ligne du fichier source
    for line in src_file:
      stripped_line = line.strip()
      # Si nous sommes à la première ligne
      if first_line and stripped_line:
        new_line = '<h1>' + stripped_line + '</h1>\n'
        first_line = False
      # Sinon, vérifier si la ligne commence par un chiffre suivi d'un point
      elif stripped_line and stripped_line[0].isdigit() and stripped_line[1] == '.':
        # Si nous ne sommes pas déjà dans une liste, ajouter une balise <ul>
        if not in_list:
          dest_file.write('<ul>\n')
          in_list = True
        # Envelopper la ligne dans des balises <li>
        new_line = '  <li>' + stripped_line[2:].strip() + '</li>\n'
      else:
        # Si nous étions dans une liste, ajouter une balise </ul>
        if in_list:
          dest_file.write('</ul>\n')
          in_list = False
        # Envelopper la ligne dans des balises <p> (si la ligne n'est pas vide)
        if stripped_line:
          new_line = '<p>' + stripped_line + '</p>\n'
        else:
          new_line = '\n'
      # Écrire la nouvelle ligne dans le fichier de destination
      dest_file.write(new_line)
    # Si le fichier se termine par une liste, ajouter une balise </ul>
    if in_list:
      dest_file.write('</ul>\n')