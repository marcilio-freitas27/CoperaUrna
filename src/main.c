#include <stdio.h>
#include <locale.h>

main () 
{
	setlocale(LC_ALL, "Portuguese");
	
    int eleitor, v, e, branco, nulo, can1, can2, can3;
    eleitor = 1;
    v = 0;
    branco = 0;
    nulo = 0;
    can1 = 0;
    can2 = 0;
    can3 = 0;
    while (eleitor <= 5)
    {
    printf("Candidatos e seus respectivos números:\n");
    printf("Candidato Fulano = 1 \n");
    printf("Candidato Cicrano = 2 \n");
    printf("Candidato Azucrino = 3 \n");
    printf("Nulo = 4 \n");
    
    printf("O registro do seu voto é: %d \n\n", eleitor);
    printf("Digite o número do seu candidato: ");
    scanf("%d", &v);
	    switch(v) 
        {
            case 1:
                printf("Você votou no candidato Fulano. \n");
                can1 += 1;
                break;
                
            case 2:
                printf("Você votou no candidato Cicrano. \n");
                can2 += 1;
                break;
            
            case 3:
                printf("Você votou no candidato Azucrino. \n");
                can3 += 1;
                break;
                
            case 4:
                printf("Você votou NULO! \n");
                nulo += 1;
                break;
                
            case 5:
                printf("Você votou em BRANCO! \n");
                branco += 1;
                break;
                
            default:
                printf("Opcao Invalida.\n");
                printf("Escolha um numero entre 1 e 5.");
                break;
                      
            }
            system("cls");
            eleitor +=1;
	}
		
		printf("Resultados: \n");
		printf("candidato Fulano: %d\n", can1);
		printf("candidato Cicrano: %d\n", can2);
		printf("candidato Azucrino: %d\n", can3);
		printf("votos Nulos: %d\n", nulo);
		printf("votos em branco: %d\n", branco);
		
		
		if (can1 > can2) (can1 > can3);
			if (can1 > 0);	
			printf("\n\nO Candidato eleito foi Fulano com: %d \n", can1);
			
		if (can2 > can1) (can2 > can3);
			if (can2 > 0);
			printf("O Candidato eleito foi Cicrano com: %d \n", can2);
			
		if (can3 > can1) (can3 > can2);
			if (can3 > 0);
			printf("O Candidato eleito foi Azucrino com: %d \n", can3);
			
		
		if (can1 = can2 = can3);
		printf("Houve um empate!\n\n");
		printf("Pressione qualquer tecla para continuar!");
		getch();
		system("cls");
		printf("Houve um empate, vamos ao desempate! \n");
		printf("Vote em um candidato!\n\n");
		printf("Candidatos e seus respectivos números:\n");
		    printf("Candidato Fulano = 1 \n");
		    printf("Candidato Cicrano = 2 \n");
		    printf("Candidato Azucrino = 3 \n");
		    printf("Nulo = 4 \n");
		    
		    printf("O registro do seu voto é: DESEMPATE\n\n");
		    printf("Digite o número do seu candidato: ");
		    scanf("%d", &v);
			    switch(v) 
		        {
		            case 1:
		                printf("Você votou no candidato Fulano. \n");
		                can1 += 1;
		                break;
		                
		            case 2:
		                printf("Você votou no candidato Cicrano. \n");
		                can2 += 1;
		                break;
		            
		            case 3:
		                printf("Você votou no candidato Azucrino. \n");
		                can3 += 1;
		                break;
		                
		            case 4:
		                printf("Você votou NULO! \n");
		                nulo += 1;
		                break;
		                
		            case 5:
		                printf("Você votou em BRANCO! \n");
		                branco += 1;
		                break;
		                
		            default:
		                printf("Opcao Invalida.\n");
		                printf("Escolha um numero entre 1 e 5.");
		                break;
		                      
		            }
		            
		            system("cls");

		printf("Resultados: \n");
		printf("candidato Fulano: %d\n", can1);
		printf("candidato Cicrano: %d\n", can2);
		printf("candidato Azucrino: %d\n", can3);
		printf("votos Nulos: %d\n", nulo);
		printf("votos em branco: %d\n", branco);
		
		
		if (can1 > can2) (can1 > can3);
			if (can1 > 0)	
			printf("\n\nO Candidato eleito foi Fulano com: %d \n", can1);
			return 0;
		if (can2 > can1) (can2 > can3);
			if (can2 > 0)
			printf("O Candidato eleito foi Cicrano com: %d \n", can2);
			return 0;
		if (can3 > can1) (can3 > can2);
			if (can3 > 0)
			printf("O Candidato eleito foi Azucrino com: %d \n", can3);
			return 0;
}