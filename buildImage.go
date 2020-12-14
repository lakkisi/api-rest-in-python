package main

import (
    "log"
    "os"
    "os/exec"
)

func main() {
    cmd := exec.Command("docker","build","-t","api-rest-in-python",".")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    log.Println(cmd.Run())
}