import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from datetime import datetime

class XbowIAChatBot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("X-bow.IA - Login")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        self.root.configure(bg='#0f0f23')
        
        self.center_window(500, 500)
        
        # Credenciais
        self.valid_users = {
            "admin": "123456",
            "usuario": "senha123", 
            "ti": "tecnologia",
            "dev": "developer"
        }
        
        # Base de conhecimento
        self.knowledge_base = self.create_knowledge_base()
        
        # Configuração de temas
        self.dark_mode = True
        self.colors = {
            "light": {
                "bg": "#ffffff", "fg": "#2c3e50", "primary": "#8B5FBF", "secondary": "#6A4C93",
                "accent": "#FF6B6B", "success": "#27ae60", "text_bg": "#f8f9fa", "entry_bg": "#ecf0f1",
                "chat_user_bg": "#8B5FBF", "chat_user_fg": "white", "chat_bot_bg": "#FF6B6B", "chat_bot_fg": "white",
                "card_bg": "#ffffff"
            },
            "dark": {
                "bg": "#0f0f23", "fg": "#e0e0e0", "primary": "#8B5FBF", "secondary": "#6A4C93", 
                "accent": "#FF6B6B", "success": "#27ae60", "text_bg": "#1a1a2e", "entry_bg": "#2d2d44",
                "chat_user_bg": "#8B5FBF", "chat_user_fg": "white", "chat_bot_bg": "#FF6B6B", "chat_bot_fg": "white",
                "card_bg": "#1a1a2e"
            }
        }
        
        self.current_theme = self.colors["dark"]
        self.create_login_screen()
    
    def create_knowledge_base(self):
        return {
            "python": {
                "resposta": "Python - Linguagem versatil\n\n• Criador: Guido van Rossum (1991)\n• Uso: Web, Dados, IA, Automacao\n• Frameworks: Django, Flask, FastAPI\n• Bibliotecas: Pandas, NumPy, TensorFlow\n• Exemplo: print('Hello World!')",
                "tags": ["programacao", "web", "dados", "ia"]
            },
            "javascript": {
                "resposta": "JavaScript - A linguagem da web\n\n• Criador: Brendan Eich (1995)\n• Uso: Frontend, Backend (Node.js)\n• Frameworks: React, Vue, Angular\n• Exemplo: console.log('Hello World!')",
                "tags": ["web", "frontend", "backend", "node"]
            },
            "java": {
                "resposta": "Java - Linguagem corporativa\n\n• Criador: James Gosling (1995)\n• Plataforma: JVM\n• Uso: Android, Sistemas Enterprise\n• Exemplo: System.out.println('Hello World!');",
                "tags": ["empresarial", "android", "jvm"]
            },
            "html": {
                "resposta": "HTML - Estrutura web\n\n• Uso: Estruturacao de paginas web\n• Elementos: Tags, atributos\n• Exemplo: <h1>Hello World!</h1>",
                "tags": ["web", "frontend", "estrutura"]
            },
            "css": {
                "resposta": "CSS - Estilo e design\n\n• Uso: Estilizacao e layout\n• Recursos: Flexbox, Grid, Animações\n• Exemplo: .classe { color: blue; }",
                "tags": ["web", "estilo", "design"]
            },
            "react": {
                "resposta": "React - UI componentizada\n\n• Criador: Facebook\n• Conceito: Componentes reutilizaveis\n• Recursos: Hooks, JSX, Virtual DOM\n• Exemplo: function App() { return <h1>Hello</h1>; }",
                "tags": ["frontend", "ui", "components"]
            },
            "node.js": {
                "resposta": "Node.js - JavaScript no servidor\n\n• Criador: Ryan Dahl (2009)\n• Runtime: V8 engine\n• Uso: APIs, Microservices\n• Exemplo: const http = require('http');",
                "tags": ["javascript", "backend", "api"]
            },
            "docker": {
                "resposta": "Docker - Containerizacao\n\n• Conceito: Empacotar app + dependencias\n• Comandos: docker run, docker build\n• Vantagens: Portabilidade, consistencia",
                "tags": ["containers", "devops", "deploy"]
            },
            "git": {
                "resposta": "Git - Controle de versao\n\n• Criador: Linus Torvalds\n• Comandos: commit, push, pull, branch\n• Plataformas: GitHub, GitLab",
                "tags": ["versionamento", "colaboracao"]
            },
            "sql": {
                "resposta": "SQL - Banco de dados relacional\n\n• Uso: Gerenciar bancos relacionais\n• Comandos: SELECT, INSERT, UPDATE\n• Exemplo: SELECT * FROM usuarios;",
                "tags": ["banco", "dados", "relacional"]
            },
            "dev experience": {
                "resposta": "Developer Experience (DX)\n\n• Definicao: Experiencia do desenvolvedor\n• Pilares: Documentacao, Ferramentas, Feedback\n• Exemplos: VSCode, Docker, Git",
                "tags": ["dx", "produtividade", "ferramentas"]
            },
            "lua": {
                "resposta": "Lua - Scripting leve\n\n• Uso: Game development, Embedded\n• Vantagens: Leve (200KB), rapida\n• Exemplo: print('Hello World')",
                "tags": ["scripting", "games", "leve"]
            },
            "julia": {
                "resposta": "Julia - Cientifica e Rapida\n\n• Foco: Computacao cientifica\n• Performance: Quase como C\n• Uso: Data science, Machine learning",
                "tags": ["ciencia", "dados", "performance"]
            }
        }
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_login_screen(self):
        self.clear_screen()
        
        # Container principal
        main_frame = tk.Frame(self.root, bg=self.current_theme['bg'], padx=40, pady=40)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Logo/Header
        header_frame = tk.Frame(main_frame, bg=self.current_theme['bg'])
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        logo_label = tk.Label(header_frame, 
                            text="X-bow.IA", 
                            font=("Arial", 32, "bold"), 
                            fg=self.current_theme['primary'],
                            bg=self.current_theme['bg'])
        logo_label.pack()
        
        subtitle_label = tk.Label(header_frame, 
                                text="Assistente de TI Inteligente", 
                                font=("Arial", 14), 
                                fg=self.current_theme['fg'],
                                bg=self.current_theme['bg'])
        subtitle_label.pack(pady=(15, 0))
        
        # Card de login
        login_card = tk.Frame(main_frame, 
                            bg=self.current_theme['card_bg'], 
                            relief='flat',
                            borderwidth=0,
                            highlightbackground=self.current_theme['primary'],
                            highlightthickness=2,
                            padx=40, 
                            pady=40)
        login_card.pack(fill=tk.BOTH, expand=True, pady=20)
        
        card_title = tk.Label(login_card, 
                            text="Acesso ao Sistema", 
                            font=("Arial", 22, "bold"), 
                            fg=self.current_theme['primary'],
                            bg=self.current_theme['card_bg'])
        card_title.pack(pady=(0, 40))
        
        # Campos do formulário
        form_frame = tk.Frame(login_card, bg=self.current_theme['card_bg'])
        form_frame.pack(fill=tk.X)
        
        # Campo usuário
        user_frame = tk.Frame(form_frame, bg=self.current_theme['card_bg'])
        user_frame.pack(fill=tk.X, pady=20)
        
        user_label = tk.Label(user_frame, 
                            text="Usuario", 
                            font=("Arial", 12, "bold"), 
                            fg=self.current_theme['fg'],
                            bg=self.current_theme['card_bg'])
        user_label.pack(anchor="w", pady=(0, 8))
        
        self.user_entry = tk.Entry(user_frame, 
                                font=("Arial", 14), 
                                bg=self.current_theme['entry_bg'],
                                fg=self.current_theme['fg'],
                                relief='flat',
                                insertbackground=self.current_theme['fg'],
                                width=25)
        self.user_entry.pack(fill=tk.X, ipady=12)
        
        # Campo senha
        pass_frame = tk.Frame(form_frame, bg=self.current_theme['card_bg'])
        pass_frame.pack(fill=tk.X, pady=20)
        
        pass_label = tk.Label(pass_frame, 
                            text="Senha", 
                            font=("Arial", 12, "bold"), 
                            fg=self.current_theme['fg'],
                            bg=self.current_theme['card_bg'])
        pass_label.pack(anchor="w", pady=(0, 8))
        
        self.pass_entry = tk.Entry(pass_frame, 
                                font=("Arial", 14), 
                                bg=self.current_theme['entry_bg'],
                                fg=self.current_theme['fg'],
                                show="*",
                                relief='flat',
                                insertbackground=self.current_theme['fg'],
                                width=25)
        self.pass_entry.pack(fill=tk.X, ipady=12)
        
        # Botão de login
        login_btn = tk.Button(form_frame, 
                            text="Entrar no X-bow.IA", 
                            font=("Arial", 14, "bold"), 
                            bg=self.current_theme['primary'],
                            fg="white",
                            relief='flat',
                            cursor='hand2',
                            padx=30,
                            pady=15,
                            command=self.verify_login)
        login_btn.pack(fill=tk.X, pady=30)
        
        # Dicas
        tips_frame = tk.Frame(main_frame, bg=self.current_theme['bg'])
        tips_frame.pack(fill=tk.X, pady=(20, 0))
        
        tips_label = tk.Label(tips_frame, 
                            text="Dica: Use admin/123456", 
                            font=("Arial", 11), 
                            fg=self.current_theme['fg'],
                            bg=self.current_theme['bg'])
        tips_label.pack()
        
        # Bind Enter key
        self.user_entry.bind('<Return>', lambda e: self.pass_entry.focus())
        self.pass_entry.bind('<Return>', lambda e: self.verify_login())
        
        self.user_entry.focus()
    
    def verify_login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        
        if username in self.valid_users and self.valid_users[username] == password:
            self.current_user = username
            self.create_chat_screen()
        else:
            messagebox.showerror("Erro", "Usuario ou senha invalidos!")
    
    def get_ai_response(self, message):
        message_lower = message.lower()
        
        # Busca direta
        for termo, info in self.knowledge_base.items():
            if termo in message_lower:
                return info["resposta"]
        
        # Busca por tags
        for termo, info in self.knowledge_base.items():
            for tag in info["tags"]:
                if tag in message_lower:
                    return info["resposta"]
        
        # Respostas contextuais
        if "oi" in message_lower or "ola" in message_lower:
            return "Ola! Sou o X-bow.IA, seu assistente de TI!\n\nPosso ajudar com: Python, JavaScript, Java, React, Docker, Git, SQL e muito mais!\n\nPergunte sobre qualquer tecnologia!"
        
        if "obrigado" in message_lower:
            return "De nada! Estou aqui para ajudar!"
        
        # Resposta padrao
        return "Desculpe, nao tenho informacoes sobre isso no momento.\n\nPosso ajudar com: Python, JavaScript, Java, HTML, CSS, React, Node.js, Docker, Git, SQL, Lua, Julia e Dev Experience."
    
    def create_chat_screen(self):
        self.clear_screen()
        self.root.title(f"X-bow.IA - {self.current_user}")
        self.root.geometry("1000x700")
        self.center_window(1000, 700)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.current_theme['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.current_theme['primary'], height=80)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        header_frame.pack_propagate(False)
        
        header_content = tk.Frame(header_frame, bg=self.current_theme['primary'])
        header_content.pack(fill=tk.BOTH, expand=True, padx=25, pady=15)
        
        title_label = tk.Label(header_content, 
                            text="X-bow.IA", 
                            font=("Arial", 22, "bold"), 
                            fg="white",
                            bg=self.current_theme['primary'])
        title_label.pack(side=tk.LEFT)
        
        status_label = tk.Label(header_content, 
                              text="Modo Local - Pronto!", 
                              font=("Arial", 11, "bold"), 
                              fg="white",
                              bg=self.current_theme['primary'])
        status_label.pack(side=tk.LEFT, padx=25)
        
        user_info = tk.Label(header_content, 
                            text=f"Usuario: {self.current_user}", 
                            font=("Arial", 14), 
                            fg="white",
                            bg=self.current_theme['primary'])
        user_info.pack(side=tk.RIGHT)
        
        # Área do chat
        chat_container = tk.Frame(main_frame, bg=self.current_theme['text_bg'], relief='flat', borderwidth=0)
        chat_container.pack(fill=tk.BOTH, expand=True)
        
        self.chat_area = scrolledtext.ScrolledText(
            chat_container, 
            wrap=tk.WORD, 
            width=80, 
            height=25,
            font=("Arial", 12),
            bg=self.current_theme['text_bg'],
            fg=self.current_theme['fg'],
            relief='flat',
            borderwidth=0,
            padx=25,
            pady=25,
            insertbackground=self.current_theme['fg']
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        self.chat_area.config(state=tk.DISABLED)
        
        # Frame de entrada
        input_frame = tk.Frame(main_frame, bg=self.current_theme['bg'], height=80)
        input_frame.pack(fill=tk.X, pady=(15, 0))
        input_frame.pack_propagate(False)
        
        input_content = tk.Frame(input_frame, bg=self.current_theme['bg'])
        input_content.pack(fill=tk.BOTH, expand=True, padx=5, pady=8)
        
        self.message_entry = tk.Entry(input_content, 
                                    font=("Arial", 14), 
                                    bg=self.current_theme['entry_bg'],
                                    fg=self.current_theme['fg'],
                                    relief='flat',
                                    insertbackground=self.current_theme['fg'])
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 15), ipady=10)
        self.message_entry.bind('<Return>', lambda e: self.send_message())
        
        # Botões
        btn_frame = tk.Frame(input_content, bg=self.current_theme['bg'])
        btn_frame.pack(side=tk.RIGHT)
        
        send_btn = tk.Button(btn_frame, 
                            text="Enviar", 
                            font=("Arial", 12, "bold"), 
                            bg=self.current_theme['success'],
                            fg="white",
                            relief='flat',
                            cursor='hand2',
                            padx=20,
                            pady=12,
                            command=self.send_message)
        send_btn.pack(side=tk.LEFT, padx=8)
        
        clear_btn = tk.Button(btn_frame, 
                            text="Limpar", 
                            font=("Arial", 12), 
                            bg=self.current_theme['accent'],
                            fg="white",
                            relief='flat',
                            cursor='hand2',
                            padx=20,
                            pady=12,
                            command=self.clear_chat)
        clear_btn.pack(side=tk.LEFT, padx=8)
        
        theme_btn = tk.Button(btn_frame, 
                            text="Tema", 
                            font=("Arial", 12), 
                            bg=self.current_theme['secondary'],
                            fg="white",
                            relief='flat',
                            cursor='hand2',
                            padx=20,
                            pady=12,
                            command=self.toggle_theme)
        theme_btn.pack(side=tk.LEFT, padx=8)
        
        # Configurar formatação
        self.setup_chat_tags()
        
        # Mensagem de boas-vindas
        welcome_msg = """X-bow.IA - Assistente de TI

Conhecimento em:
• Python, JavaScript, Java
• HTML, CSS, React, Node.js
• Docker, Git, SQL
• Lua, Julia
• Dev Experience

Exemplos de perguntas:
"O que é Python?"
"Como funciona Docker?"
"Explique React"
"O que é Lua?"

Pergunte sobre qualquer tecnologia!"""

        self.add_message("X-bow.IA", welcome_msg, is_user=False)
        
        self.message_entry.focus()
    
    def setup_chat_tags(self):
        self.chat_area.tag_configure("user_name", 
                                   font=("Arial", 11, "bold"), 
                                   foreground=self.current_theme['chat_user_bg'])
        self.chat_area.tag_configure("bot_name", 
                                   font=("Arial", 11, "bold"), 
                                   foreground=self.current_theme['chat_bot_bg'])
        self.chat_area.tag_configure("user_msg", 
                                   font=("Arial", 12), 
                                   lmargin1=20, 
                                   lmargin2=20,
                                   rmargin=10,
                                   foreground=self.current_theme['fg'])
        self.chat_area.tag_configure("bot_msg", 
                                   font=("Arial", 12), 
                                   lmargin1=20, 
                                   lmargin2=20,
                                   rmargin=10,
                                   foreground=self.current_theme['fg'])
        self.chat_area.tag_configure("timestamp", 
                                   font=("Arial", 9), 
                                   foreground="#7f8c8d")
    
    def send_message(self):
        message = self.message_entry.get().strip()
        if not message:
            return
        
        self.add_message(self.current_user, message, is_user=True)
        self.message_entry.delete(0, tk.END)
        
        self.show_typing_indicator()
        self.root.after(1000, self.generate_response, message)
    
    def show_typing_indicator(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"\nX-bow.IA esta digitando...\n", "timestamp")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)
        self.root.update()
    
    def generate_response(self, user_message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete("end-2l", "end-1l")
        self.chat_area.config(state=tk.DISABLED)
        
        response = self.get_ai_response(user_message)
        self.add_message("X-bow.IA", response, is_user=False)
    
    def add_message(self, sender, message, is_user=True):
        self.chat_area.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M")
        
        if is_user:
            self.chat_area.insert(tk.END, f"\n{sender}", "user_name")
            self.chat_area.insert(tk.END, f" • {timestamp}\n", "timestamp")
            self.chat_area.insert(tk.END, f"{message}\n", "user_msg")
        else:
            self.chat_area.insert(tk.END, f"\n{sender}", "bot_name")
            self.chat_area.insert(tk.END, f" • {timestamp}\n", "timestamp")
            self.chat_area.insert(tk.END, f"{message}\n", "bot_msg")
        
        self.chat_area.insert(tk.END, "-" * 80 + "\n", "timestamp")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)
    
    def clear_chat(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)
        
        welcome_msg = "Conversa reiniciada! X-bow.IA pronto para ajudar!"
        self.add_message("X-bow.IA", welcome_msg, is_user=False)
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.current_theme = self.colors["dark"] if self.dark_mode else self.colors["light"]
        self.apply_theme()
    
    def apply_theme(self):
        if hasattr(self, 'current_user'):
            self.create_chat_screen()
        else:
            self.create_login_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        self.root.mainloop()

# Executar
if __name__ == "__main__":
    app = XbowIAChatBot()
    app.run()