import mdprocessing
import copystatic as cs
import generatepage as gp

def main():
    cs.copy_static("static", "public")
    gp.generate_page_recursive("content", "public", "template.html")
        
if __name__ == "__main__": 
    main()