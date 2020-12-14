package main

import (
    "log"
    "os"
    "os/exec"
)

func main() {
    cmd := exec.Command("docker","run","-p","5000:5000","-d","api-rest-in-python")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    log.Println(cmd.Run())
}