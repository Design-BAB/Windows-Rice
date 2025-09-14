:set mouse=a
set expandtab
set shiftwidth=4
set tabstop=4
set hidden
set signcolumn=yes:2
set relativenumber
set number
set termguicolors
set undofile
set spell
set title
set ignorecase
set smartcase
set wildmode=longest:full,full
set nowrap
set list
set mouse=a
set scrolloff=8
set sidescrolloff=8
set nojoinspaces
set splitright
set clipboard=unnamedplus
set confirm
set exrc

call plug#begin('~/.local/share/nvim/plugged')
Plug 'neoclide/coc.nvim', {'do': 'yarn install --frozen-lockfile && yarn build'}
Plug 'fatih/vim-go'
Plug 'charlespascoe/vim-go-syntax'
Plug 'preservim/nerdtree'
call plug#end()

set hidden
set cmdheight=2
set updatetime=300
set shortmess+=c
set signcolumn=yes

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use `[c` and `]c` to navigate diagnostics
nmap <silent> [c <Plug>(coc-diagnostic-prev)
nmap <silent> ]c <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use U to show documentation in preview window
nnoremap <silent> U :call <SID>show_documentation()<CR>

" Remap for rename current word
nmap <leader>rn <Plug>(coc-rename)

" Remap for format selected region
vmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)
" Show all diagnostics
nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions
nnoremap <silent> <space>x  :<C-u>CocList extensions<cr>
" Show commands
nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document
nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols
nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list
nnoremap <silent> <space>p  :<C-u>CocListResume<CR>
let g:go_def_mapping_enabled = 0
syntax on
" Use Tab to select next item in autocomplete
inoremap <silent><expr> <Tab> pumvisible() ? coc#pum#next(1) : "\<Tab>"

" Use Shift-Tab to select previous item
inoremap <silent><expr> <S-Tab> pumvisible() ? coc#pum#prev(1) : "\<C-h>"

" Use Enter to confirm selection
inoremap <silent><expr> <CR> pumvisible() ? coc#pum#confirm() : "\<CR>"

nnoremap <silent> <leader>e :NERDTreeToggle<CR>

command! GoRunIt :terminal go run %
