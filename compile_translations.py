"""
Script pour compiler les fichiers de traduction au format .mo
"""
import os
import subprocess
import sys

def compile_translations():
    """Compile les fichiers .po en fichiers .mo sans utiliser pybabel"""
    try:
        # Utiliser une approche alternative en important directement le module babel
        from babel.messages.mofile import write_mo
        from babel.messages.pofile import read_po
        
        languages = ['fr', 'en']
        
        for lang in languages:
            po_file = f'translations/{lang}/LC_MESSAGES/messages.po'
            mo_file = f'translations/{lang}/LC_MESSAGES/messages.mo'
            
            if os.path.exists(po_file):
                print(f"Compilation du fichier {po_file}...")
                with open(po_file, 'rb') as po_input:
                    catalog = read_po(po_input)
                
                with open(mo_file, 'wb') as mo_output:
                    write_mo(mo_output, catalog)
                    
                print(f"Fichier {mo_file} créé avec succès.")
            else:
                print(f"Le fichier {po_file} n'existe pas.")
        
        print("Compilation des traductions terminée.")
                
    except ImportError:
        print("Erreur: Module babel non trouvé. Veuillez l'installer avec 'pip install babel'.")
        return False
    except Exception as e:
        print(f"Erreur lors de la compilation des traductions: {e}")
        return False
    
    return True

if __name__ == "__main__":
    compile_translations()
