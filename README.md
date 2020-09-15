# Introduction
This repository is a CBL-Mariner derivative repo for personal experimentation

## Extract toolkit
Download the `toolkit.tar.gz` file to disk, then:
```bash
cd ~/derivative-experiments
tar -xzf ~/toolkit.tar.gz
```

## Build VHDX
```bash
cd toolkit
sudo make image CONFIG_FILE=../imageconfigs/demo_vhdx.json
```

## Output Files
The sample package `hello_world-demo-*.x86_64.rpm` can be found in `~/demo/out/RPMS/x86_64/` along with all the other packages which were needed for image generation.

`minimal_demo.vhdx` can be found in ``~/demo/out/images/`

