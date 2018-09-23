call plug#begin('~/.config/nvim/autoload/plugged')
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' } 
"Plug 'Alvarocz/vim-northpole'
Plug 'dikiaap/minimalist'
Plug 'junegunn/vim-easy-align'
Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
call plug#end()

set t_Co=256
syntax on
colorscheme minimalist

let g:airline_theme='minimalist'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1


" Spaces & Tabs {{{
set tabstop=4       " number of visual spaces per TAB
set softtabstop=4   " number of spaces in tab when editing
set shiftwidth=4    " number of spaces to use for autoindent
set expandtab       " tabs are space
set autoindent
set copyindent      " copy indent from the previous line
" }}} Spaces & Tabs


set number

let g:python3_host_prog = '/usr/bin/python3'
