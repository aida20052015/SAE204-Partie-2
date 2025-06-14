<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class SiemensController extends AbstractController
{
    #[Route('/siemens', name: 'app_siemens')]
    public function index(): Response
    {
        // Exécute le script Python
        $output = [];
        $return_var = 0;
        exec('python3 scripts/codeameliore.py', $output, $return_var);

        return $this->render('siemens/index.html.twig', [
            'image_path' => 'etoile.png',
        ]);
    }
}
