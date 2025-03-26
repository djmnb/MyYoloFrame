我希望每次都能保留每个类的ap的输出到文件中, 只需要修改ultralytics/models/yolo/detect/val.py的print_results函数即可:
```python
    def print_results(self):
        """Print training/validation set metrics per class."""
        write_data = []
       
        write_data.append(self.get_desc())
        pf = "%22s" + "%11i" * 2 + "%11.3g" * len(self.metrics.keys)  # print format
        
        out = pf % ("all", self.seen, self.nt_per_class.sum(), *self.metrics.mean_results())
        LOGGER.info(out)
        write_data.append(out)
        
        if self.nt_per_class.sum() == 0:
            LOGGER.warning(f"WARNING ⚠️ no labels found in {self.args.task} set, can not compute metrics without labels")

        # Print results per class
        if self.args.verbose and not self.training and self.nc > 1 and len(self.stats):
            for i, c in enumerate(self.metrics.ap_class_index):
                out = pf % (self.names[c], self.nt_per_image[c], self.nt_per_class[c], *self.metrics.class_result(i))
                LOGGER.info(
                    out
                )
                write_data.append(out)

        if self.args.plots:
            for normalize in True, False:
                self.confusion_matrix.plot(
                    save_dir=self.save_dir, names=self.names.values(), normalize=normalize, on_plot=self.on_plot
                )
        if self.save_dir:
            with open(self.save_dir / "ap_results.txt", "w") as f:
                f.write("\n".join(write_data))


