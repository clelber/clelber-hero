
**Documentação de uso da API clelber-hero, criado para teste prático em processo seletivo**


**Para facilitar o acesso as rotas de forma mais genérica e descomplicada, utilizei o recursos de "SimpleRouter",
presente no Django Rest Framework**


----------------------------------------------------------------
**para criação de nova empresa**

URI: https://clelber-hero.herokuapp.com/api/ev1/empresas/

media type: appication/json
method: post

modelo json para gravação de nova empresa

{
    "nome": "",
    "cnpj": "",
    "ativo": true
}
-----------------------------------------------------------------

**para listagem das empresas com seus funcionários**

URI: https://clelber-hero.herokuapp.com/api/ev1/empresas/
method: get


-----------------------------------------------------------------

**para criação de novo funcionário**

URI: https://clelber-hero.herokuapp.com/api/fv1/funcionarios/

modelo json para criação de novo funcionário

{
    "nome": "",
    "cpf": "",
    "empresas": []
}
-------------------------------------------------------------------

**para listagem dos funcionarios e suas empresas**

URI: https://clelber-hero.herokuapp.com/api/fv1/funcionarios/
method: get


-------------------------------------------------------------------


**para listagem de todos os funcionários de uma determinada empresa**

URI:https://clelber-hero.herokuapp.com/api/ev1/empresas/empresa_id/funcionarios/

passando o ID da empresa em questão no parâmetro "empresa_id"

---------------------------------------------------------------------


caso seja necessário acesso ao painel de administração do Django

URI: https://clelber-hero.herokuapp.com/admin/

usuário: clelber
senha: 123456







